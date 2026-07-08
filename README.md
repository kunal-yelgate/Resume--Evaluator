# ⚡ ResumeAI — Smart Resume Analyzer

An AI-powered resume evaluation tool that analyzes resumes, identifies skills, detects gaps, generates personalized learning roadmaps, and prepares interview questions based on your target role.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

- **AI-Powered Analysis** — Uses Groq's LLaMA 3.3 70B to evaluate resume content against your career goals
- **Skill Detection** — Automatically extracts and identifies your current technical skills
- **Gap Analysis** — Identifies missing skills required for your target role
- **Learning Roadmap** — Generates step-by-step learning paths to bridge skill gaps
- **Interview Prep** — Creates tailored interview questions based on your profile
- **File Upload Support** — Accepts PDF and DOCX resume uploads
- **Analysis History** — Saves all past analyses for future reference
- **Secure Authentication** — User registration and login system with password hashing
- **Responsive UI** — Clean, modern interface optimized for all devices

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: MySQL (via PyMySQL)
- **AI Engine**: Groq API (LLaMA 3.3 70B)
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Document Parsing**: PyPDF2, python-docx

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL database
- Groq API key ([Get one here](https://console.groq.com/keys))

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kunal-yelgate/ResumeAI_Evaluator.git
   cd ResumeAI_Evaluator
