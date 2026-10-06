# 🎯 SkillSync

### Personalized Skill & Career Development Platform

SkillSync is a web-based skill and career development platform designed to help students understand their current skills, identify skill gaps, and prepare for their desired career roles.

The application allows users to create a basic profile, select their current skills, choose a target career, analyze the skills required for that career, and receive personalized recommendations.

---

## 📌 Project Overview

Students often have difficulty understanding which skills they need to develop for a particular career. SkillSync solves this problem by comparing a user's existing skills with the skills required for their selected career role.

The system provides:

- User profile management
- Current skill selection
- Target career selection
- Skill gap analysis
- Skill recommendations
- Learning roadmap
- Skill progress tracking
- Career readiness score
- Career profile summary

The goal of SkillSync is to provide students with a simple and interactive platform for planning their technical skill development.

---

## 🎯 Objectives

The main objectives of SkillSync are:

1. To help students identify their current technical skills.
2. To understand the skills required for a particular career.
3. To identify missing or weak skills.
4. To provide personalized skill recommendations.
5. To create a structured learning roadmap.
6. To track skill development progress.
7. To calculate a career readiness score.
8. To provide an overall career profile summary.

---

## 🚀 Features

### 👤 User Profile

Users can enter basic information such as:

- Name
- Course
- Year of study

### 💻 Skill Selection

Users can select the technical skills they currently possess, such as:

- Python
- Java
- C
- C++
- HTML
- CSS
- JavaScript
- SQL
- Git
- Machine Learning
- Data Structures
- Problem Solving

### 🎯 Career Selection

Users can select a target career role, including:

- Software Developer
- Data Scientist
- Machine Learning Engineer
- Web Developer
- Data Analyst

### 📊 Skill Gap Analysis

SkillSync compares the user's current skills with the skills required for their selected career.

It identifies:

- Skills the user already has
- Skills that still need to be learned

### 🎯 Skill Recommendations

The application provides recommendations for missing skills and explains what the user should focus on learning.

### 🗺️ Learning Roadmap

SkillSync provides a step-by-step learning roadmap for important missing skills.

### 📈 Progress Tracker

Users can mark required skills as completed and monitor their learning progress.

### 🏆 Career Readiness Score

The application calculates a percentage-based career readiness score according to the number of required skills the user currently possesses.

### 📄 Career Profile Summary

The application generates a summary containing:

- User information
- Current skills
- Target career
- Missing skills
- Career readiness score

### 🎨 User Interface

SkillSync uses Streamlit with a customized interface containing:

- Gradient backgrounds
- Styled sidebar
- Modern headings
- Cards and metrics
- Progress indicators
- Interactive input components

---

## 🛠️ Technologies Used

### Programming Language

- Python 3.11.9

### Framework

- Streamlit

### Data & Machine Learning

- Pandas
- NumPy
- Scikit-learn

### Natural Language Processing

- NLTK
- spaCy

### AI / NLP

- Transformers
- Sentence Transformers
- Google GenAI
- LangChain
- LangChain Community

### Other Libraries

- Requests
- Python-dotenv
- PyTorch

---

## 📂 Project Structure

```text
SkillSync/
│
├── .venv/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |
| `.venv/` | Python virtual environment |

---

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\activate
```

If PowerShell blocks activation, the environment can also be used directly through its Python executable.

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command from the SkillSync project folder:

```bash
streamlit run app.py
```

The application will open in a web browser.

---

## 🔄 How SkillSync Works

```text
User Profile
     ↓
Current Skills
     ↓
Target Career
     ↓
Required Skills
     ↓
Skill Gap Analysis
     ↓
Skill Recommendations
     ↓
Learning Roadmap
     ↓
Progress Tracking
     ↓
Career Readiness Score
     ↓
Career Profile Summary
```

---

## 📊 Example

A student selects:

```text
Course: BTech CSE
Year: 1st Year

Current Skills:
Python
SQL
Git

Target Career:
Software Developer
```

SkillSync compares these skills with the requirements for a Software Developer and identifies the remaining skills that the student should learn.

The application then provides recommendations, a learning roadmap, progress tracking, and a career readiness score.

---

## 🔮 Future Enhancements

Future versions of SkillSync can include:

- AI-powered career recommendations
- Resume analysis
- Job-role recommendations
- Real-time learning resources
- Personalized course recommendations
- Advanced machine learning-based skill matching
- Skill assessment quizzes
- Resume generation
- Job description analysis
- GitHub profile analysis
- User login and database storage
- Progress history and analytics

---

## 🔐 Security

API keys and sensitive credentials should not be stored directly inside the source code.

Environment variables can be used through a `.env` file for securely managing API credentials.

The `.env` file should not be uploaded to GitHub.

---

## 🎓 Project Purpose

SkillSync is developed as an academic and learning project to demonstrate the use of Python, Streamlit, data processing, machine learning concepts, and AI technologies in solving a practical student career-development problem.

---

## 👨‍💻 Author

**SkillSync Project**

A student-focused platform for identifying skill gaps and improving career readiness.

---

## 📜 License

This project is created for educational and academic purposes.