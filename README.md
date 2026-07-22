# ⚡ ResumeAI — Smart Resume Analyzer

An AI-powered resume evaluation platform that analyzes resumes, identifies skills, detects career gaps, generates personalized learning roadmaps, and prepares interview questions based on a target role.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA%203.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

---

## 📖 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Demo / Screenshots](#-demo--screenshots)
- [Prerequisites](#-prerequisites)
- [Installation](#️-installation-guide)
- [Environment Variables](#-environment-variables)
- [Database Setup](#️-database-setup)
- [Running the App](#️-run-application)
- [Project Structure](#-project-structure)
- [How to Use](#-how-to-use)
- [AI Architecture](#-ai-architecture)
- [Security](#-security-features)
- [Error Handling](#-error-handling)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Troubleshooting / FAQ](#-troubleshooting--faq)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Features

### 🤖 AI Resume Analysis
- Uses **Groq LLaMA 3.3 70B** for intelligent resume evaluation
- Compares resume skills against target job requirements
- Generates structured, AI-based feedback

### 🧠 Skill Intelligence
- Automatically extracts technical skills
- Detects missing skills for desired roles
- Provides actionable improvement recommendations

### 🗺️ Personalized Learning Roadmap
- Generates a step-by-step learning path
- Prioritizes skills based on career goals
- Helps users prepare for industry requirements

### 🎯 Interview Preparation
- Generates role-specific interview questions
- Covers both technical and behavioral preparation

### 📄 Resume Upload Support
- PDF resumes
- DOCX resumes
- Direct text input

### 🔐 User Management
- User registration and login
- Secure password hashing
- Personal analysis history

### 📱 Modern UI
- Responsive dashboard
- Clean, minimal interface
- Mobile-friendly design

---

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python, Flask, SQLAlchemy, PyMySQL |
| **Database** | MySQL |
| **AI** | Groq API, LLaMA 3.3 70B Versatile |
| **Frontend** | HTML5, CSS3, Jinja2 Templates |
| **Document Processing** | PyPDF2, python-docx |

---

## 🎬 Demo / Screenshots

> Add screenshots or a short GIF/video walkthrough of the dashboard, resume upload, and analysis results here so visitors can see the tool in action without installing it.

```
docs/screenshots/dashboard.png
docs/screenshots/analysis-result.png
```

---

## 📋 Prerequisites

Before running the project, install:

- Python 3.8+
- MySQL Database (running instance, local or hosted)
- Git
- A Groq API key → [console.groq.com/keys](https://console.groq.com/keys)

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/kunal-yelgate/ResumeAI_Evaluator.git
cd ResumeAI_Evaluator
```

### 2. Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

See [Environment Variables](#-environment-variables) below for what to fill in.

---

## 🔑 Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | MySQL connection string | `mysql+pymysql://user:pass@localhost:3306/resumeai` |
| `FLASK_SECRET_KEY` | Secret key for Flask sessions | a long random string |
| `GROQ_API_KEY` | API key for Groq LLaMA access | from console.groq.com/keys |

> ⚠️ Never commit your `.env` file. Keep secrets out of version control — `.env` should already be listed in `.gitignore`.

---

## 🗄️ Database Setup

Initialize the database tables:

```bash
python -c "from db import Base, engine; Base.metadata.create_all(bind=engine)"
```

Make sure the MySQL database referenced in `DATABASE_URL` already exists before running this command.

---

## ▶️ Run Application

Start the Flask development server:

```bash
python app.py
```

Then open:

```
http://localhost:5000
```

> For production, run behind a WSGI server such as Gunicorn or uWSGI rather than the Flask development server — see [Deployment](#-deployment).

---

## 📁 Project Structure

```
ResumeAI_Evaluator/
│
├── app.py                 # Main Flask application
├── ai.py                  # Groq AI integration
├── db.py                  # Database configuration
├── models.py              # SQLAlchemy database models
├── requirements.txt       # Python dependencies
├── .env.example            # Environment template
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

## 🎯 How to Use

1. **Create an account** — register with your email and password.
2. **Log in** — access your personal dashboard.
3. **Upload a resume** — choose PDF, DOCX, or paste text directly.
4. **Select a career goal**, e.g.:
   - Senior Python Developer
   - Machine Learning Engineer
   - Full Stack Developer
   - Data Scientist
5. **Receive AI analysis**, including:
   - ✅ Current skills
   - ❌ Missing skills
   - 🗺️ Learning roadmap
   - ❓ Interview questions

---

## 🧠 AI Architecture

ResumeAI uses Groq's **LLaMA 3.3 70B Versatile** model to analyze:

- Technical skills
- Experience level
- Industry alignment
- Missing competencies
- Learning priorities
- Interview readiness

Output is generated in structured JSON for reliable, predictable downstream processing.

---

## 🔐 Security Features

- Password hashing
- Session-based authentication
- Secure database connections
- File upload validation (type/size checks)
- Environment-based secrets management
- Centralized error handling middleware

---

## 🐛 Error Handling

- Graceful API failure handling
- Rate-limit handling for the Groq API
- Resume parsing fallback for malformed files
- Custom `404` / `500` error pages
- User-friendly error messages throughout the UI

---

## ✅ Testing

> Add details on how to run the test suite once tests are in place, e.g.:

```bash
pytest
```

Consider adding coverage for:
- Resume parsing (PDF/DOCX edge cases)
- AI response parsing/fallback logic
- Auth flows (signup, login, password reset)

---

## 📦 Deployment

Notes for deploying beyond local development:

- Run the app with a production WSGI server (e.g. `gunicorn app:app`)
- Set `FLASK_ENV=production` and disable debug mode
- Use a managed MySQL instance and store credentials as environment secrets, not in code
- Put the app behind a reverse proxy (e.g. Nginx) with HTTPS enabled

---

## ❓ Troubleshooting / FAQ

**The app can't connect to MySQL.**
Double-check `DATABASE_URL` in `.env` and confirm the database exists and the MySQL server is running.

**Groq API calls are failing.**
Verify `GROQ_API_KEY` is set correctly and that your Groq account has available quota.

**Resume upload fails.**
Confirm the file is a valid PDF or DOCX and under the configured size limit.

---

## 🚀 Roadmap

- [ ] ATS Resume Score
- [ ] GitHub Profile Analysis
- [ ] Cover Letter Generator
- [ ] Resume Improvement Suggestions
- [ ] PDF Report Export
- [ ] Multiple Language Support
- [ ] Job Description Matching

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a Pull Request

Please open an issue first for major changes so we can discuss what you'd like to do.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Kunal Yelgate**
GitHub: [github.com/kunal-yelgate](https://github.com/kunal-yelgate)

---

⭐ If you find this project useful, consider giving it a star on GitHub!
