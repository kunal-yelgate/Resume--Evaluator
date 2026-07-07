import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session, url_for
from db import engine, Base, SessionLocal
import models
import json
import PyPDF2

from ai import analyze_resume

load_dotenv(override=True)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "open123")

Base.metadata.create_all(bind=engine)


def extract_resume_text(uploaded_file):
    if not uploaded_file or not uploaded_file.filename:
        return None

    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):
        try:
            import PyPDF2

            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            return "".join(page.extract_text() or "" for page in pdf_reader.pages)
        except Exception:
            return None

    if filename.endswith(".docx"):
        try:
            import docx

            document = docx.Document(uploaded_file)
            return "\n".join(para.text for para in document.paragraphs)
        except Exception:
            return None

    return None


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.user).filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user = models.user(email=email, password=password)
        db.add(user)
        db.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.user).filter_by(email=email, password=password).first()

        if user:
            session["user"] = user.email
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))

        return "Invalid credentials"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    result = None
    resume_text = None
    user_goal = None

    if request.method == "POST":
        user_goal = request.form.get("role") or request.form.get("desired_role")
        resume_text = request.form.get("resume_text")
        resume_file = request.files.get("resume") or request.files.get("resume_file") or request.files.get("file")
        if not resume_text:
            resume_text = extract_resume_text(resume_file)

        if resume_text and user_goal:
            try:
                result = analyze_resume(resume_text, user_goal)

                db = SessionLocal()
                user = db.query(models.user).filter_by(email=session["user"]).first()

                if user is not None:
                    report = models.Reports(
                        user_id=user.id,
                        resume_text=resume_text,
                        result=json.dumps(result),
                    )
                    db.add(report)
                    db.commit()

            except Exception as e:
                result = {"error": f"AI failed to process resume: {str(e)}"}
        elif not resume_text:
            result = {"error": "Please upload a PDF or DOCX resume."}

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result,
    )


@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    db = SessionLocal()
    user = db.query(models.user).filter_by(email=session["user"]).first()

    reports_data = []
    if user is not None:
        reports = db.query(models.Reports).filter_by(user_id=user.id).all()

        for report in reports:
            try:
                parsed_result = json.loads(report.result) if report.result else {}
            except Exception:
                parsed_result = {"raw_result": report.result}

            reports_data.append(
                {
                    "resume": report.resume_text,
                    "result": parsed_result,
                }
            )

    return render_template("history.html", reports=reports_data)


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    message = None

    if request.method == "POST":
        email = request.form.get("email")
        if email:
            message = "If the account exists, password reset instructions would be sent to that email."
        else:
            message = "Please enter your email address."

    return render_template("forgot_password.html", message=message)


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)