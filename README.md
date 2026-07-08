# ⚡ ResumeAI — Smart Resume Analyzer

An AI-powered resume evaluation platform that analyzes resumes, identifies skills, detects career gaps, generates personalized learning roadmaps, and prepares interview questions based on the target role.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA%203.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

### 🤖 AI Resume Analysis
- Uses **Groq LLaMA 3.3 70B** for intelligent resume evaluation
- Compares resume skills with target job requirements
- Generates structured AI-based feedback

### 🧠 Skill Intelligence
- Automatically extracts technical skills
- Detects missing skills for desired roles
- Provides improvement recommendations

### 🗺️ Personalized Learning Roadmap
- Generates step-by-step learning paths
- Prioritizes skills based on career goals
- Helps users prepare for industry requirements

### 🎯 Interview Preparation
- Generates role-specific interview questions
- Covers technical and behavioral preparation

### 📄 Resume Upload Support
- Supports:
  - PDF resumes
  - DOCX resumes
  - Direct text input

### 🔐 User Management
- User registration and login
- Secure password hashing
- Personal analysis history

### 📱 Modern UI
- Responsive dashboard
- Clean user interface
- Mobile-friendly design

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask
- SQLAlchemy
- PyMySQL

## Database
- MySQL

## Artificial Intelligence
- Groq API
- LLaMA 3.3 70B Model

## Frontend
- HTML5
- CSS3
- Jinja2 Templates

## Document Processing
- PyPDF2
- python-docx

---

# 📋 Prerequisites

Before running the project, install:

- Python 3.8+
- MySQL Database
- Git
- Groq API Key

Get your Groq API key:

https://console.groq.com/keys

---

# ⚙️ Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/kunal-yelgate/ResumeAI_Evaluator.git

cd ResumeAI_Evaluator
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Update the values:

```env
DATABASE_URL=mysql+pymysql://username:password@host:port/database_name

FLASK_SECRET_KEY=your_secret_key

GROQ_API_KEY=your_groq_api_key
```

---

# 🗄️ Database Setup

Initialize database tables:

```bash
python -c "from db import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

# ▶️ Run Application

Start Flask server:

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

# 📁 Project Structure

```
ResumeAI_Evaluator/

│
├── app.py                 # Main Flask application
├── ai.py                  # Groq AI integration
├── db.py                  # Database configuration
├── models.py              # SQLAlchemy database models
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
│
├── static/
│   └── style.css          # CSS styling
│
└── templates/
    ├── base.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    ├── history.html
    ├── forgot_password.html
    ├── 404.html
    └── 500.html
```

---

# 🎯 How To Use

### Step 1 — Create Account
Register using your email and password.

### Step 2 — Login
Access your personal dashboard.

### Step 3 — Upload Resume

Choose one:

- Upload PDF/DOCX file
- Paste resume text manually

### Step 4 — Select Career Goal

Example:

```
Senior Python Developer
Machine Learning Engineer
Full Stack Developer
Data Scientist
```

### Step 5 — Receive AI Analysis

The system provides:

✅ Current Skills  
❌ Missing Skills  
🗺️ Learning Roadmap  
❓ Interview Questions  

---

# 🧠 AI Architecture

ResumeAI uses Groq's **LLaMA 3.3 70B Versatile model**.

The AI analyzes:

- Technical skills
- Experience level
- Industry alignment
- Missing competencies
- Learning priorities
- Interview readiness

The output is generated in structured JSON format for reliable processing.

---

# 🔐 Security Features

Implemented security measures:

- Password hashing
- Session authentication
- Secure database connection
- File upload validation
- Environment-based secrets
- Error handling middleware

---

# 🐛 Error Handling

The application includes:

- API failure handling
- Rate-limit handling
- Resume parsing fallback
- Custom error pages
- User-friendly messages

---

# 🚀 Future Improvements

Planned features:

- [ ] ATS Resume Score
- [ ] GitHub Profile Analysis
- [ ] Cover Letter Generator
- [ ] Resume Improvement Suggestions
- [ ] PDF Report Export
- [ ] Multiple Language Support
- [ ] Job Description Matching

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository

2. Create a branch:

```bash
git checkout -b feature/new-feature
```

3. Commit changes:

```bash
git commit -m "Add new feature"
```

4. Push:

```bash
git push origin feature/new-feature
```

5. Create a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Kunal Yelgate**

GitHub:

https://github.com/kunal-yelgate

---

⭐ If you like this project, consider giving it a star on GitHub!
