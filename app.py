import os
import json

from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, redirect, session, url_for
from db import engine, Base, SessionLocal
import models
import PyPDF2

from ai import analyze_resume

load_dotenv(override=True)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change_this_secret_key_please")

Base.metadata.create_all(bind=engine)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def extract_resume_text(uploaded_file):
    if not uploaded_file or not uploaded_file.filename:
        return None

    filename = uploaded_file.filename.lower()

    if filename.endswith(".pdf"):
        try:
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


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "error")
            return render_template("signup.html")

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "error")
            return render_template("signup.html")

        db = SessionLocal()
        try:
            existing_user = db.query(models.user).filter_by(email=email).first()
            if existing_user:
                flash("An account with this email already exists.", "error")
                return render_template("signup.html")

            new_user = models.user(email=email, password=password)
            db.add(new_user)
            db.commit()
            flash("Account created! Please log in.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            db.rollback()
            flash("Something went wrong. Please try again.", "error")
            return render_template("signup.html")
        finally:
            db.close()

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Please enter your email and password.", "error")
            return render_template("login.html")

        db = SessionLocal()
        try:
            found_user = db.query(models.user).filter_by(email=email, password=password).first()

            if found_user:
                session["user"] = found_user.email
                session["user_id"] = found_user.id
                flash("Welcome back!", "success")
                return redirect(url_for("dashboard"))

            flash("Incorrect email or password. Please try again.", "error")
            return render_template("login.html")
        finally:
            db.close()

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        flash("Please log in to access the dashboard.", "error")
        return redirect(url_for("login"))

    result = None

    if request.method == "POST":
        user_goal = (request.form.get("desired_role") or request.form.get("role", "")).strip()
        resume_text = request.form.get("resume_text", "").strip()
        resume_file = request.files.get("resume_file") or request.files.get("resume") or request.files.get("file")

        # Try to extract from uploaded file if no text pasted
        if not resume_text and resume_file:
            resume_text = extract_resume_text(resume_file)

        if not resume_text:
            flash("Please paste your resume text or upload a PDF/DOCX file.", "error")
        elif not user_goal:
            flash("Please enter your target role.", "error")
        else:
            try:
                result = analyze_resume(resume_text, user_goal)

                if result.get("error"):
                    flash(result["error"], "error")
                else:
                    # Save report to database
                    db = SessionLocal()
                    try:
                        found_user = db.query(models.user).filter_by(email=session["user"]).first()
                        if found_user:
                            report = models.Reports(
                                user_id=found_user.id,
                                resume_text=resume_text,
                                result=json.dumps(result),
                            )
                            db.add(report)
                            db.commit()
                    except Exception:
                        db.rollback()
                    finally:
                        db.close()

            except Exception as e:
                flash(f"AI analysis failed: {str(e)}", "error")
                result = None

    return render_template("dashboard.html", user=session["user"], result=result)


@app.route("/history")
def history():
    if "user" not in session:
        flash("Please log in to view your history.", "error")
        return redirect(url_for("login"))

    db = SessionLocal()
    try:
        found_user = db.query(models.user).filter_by(email=session["user"]).first()
        reports_data = []

        if found_user:
            reports = db.query(models.Reports).filter_by(user_id=found_user.id).order_by(models.Reports.id.desc()).all()
            for report in reports:
                try:
                    parsed_result = json.loads(report.result) if report.result else {}
                except Exception:
                    parsed_result = {}

                # Normalize missing_skills / skills_not_found keys
                if "missing_skills" in parsed_result and "skills_not_found" not in parsed_result:
                    parsed_result["skills_not_found"] = parsed_result["missing_skills"]

                reports_data.append({
                    "resume": report.resume_text,
                    "result": parsed_result,
                })

        return render_template("history.html", reports=reports_data)
    finally:
        db.close()


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        if email:
            flash("If an account with that email exists, reset instructions have been sent.", "success")
        else:
            flash("Please enter your email address.", "error")
        return redirect(url_for("forgot_password"))

    return render_template("forgot_password.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


# ─── Error Handlers ───────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)