from flask import Flask, render_template, request, redirect, session 
from db import engine, Base, SessionLocal
import models
import docx
import PyPDF2
import json

app = Flask(__name__)
app.secret_key = "open123"

Base.metadata.create_all(bind=engine)
 
#  we built a simple flask app to test the deployment of the app on heroku
app = Flask(__name__)

# we have created a simple route to test the deployment of the app
@app.route('/')  
# created home function to return a message when the route is accessed
def home() :
    # home function will return a message when the route is accessed
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('login.html')

    # signup route to render the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    db = SessionLocal()

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        # Add logic to create a new user

        existing_user = db.query(models.user).filter_by(email=email).first()
        if existing_user:
             return "User already exists"
        
        user = models.user(email=email, password=password)
        db.add(user)
        db.commit()

        return render_template("/login.html")
    return render_template("signup.html")


# login route to render the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    db = SessionLocal()

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.user).filter_by(email=email, password=password).first()
        
        if user:
            session["user"] = user.email
            return redirect('/dashboard')
        else:
            return "Invalid credentials"

    return render_template("login.html")

# we have added a main function to run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)