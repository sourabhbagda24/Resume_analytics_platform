<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020b18,50:003366,100:00cfff&height=200&section=header&text=Resume%20Analytics%20Platform&fontSize=38&fontColor=00cfff&animation=fadeIn&fontAlignY=38&desc=AI-Powered+Resume+Parser+%7C+NLP+%7C+Google+Drive&descAlignY=58&descSize=16&descColor=ffffff"/>

<img src="https://readme-typing-svg.herokuapp.com?font=Space+Mono&weight=700&size=20&duration=3000&pause=1000&color=00CFFF&center=true&vCenter=true&width=700&lines=📄+Automatically+Parse+Resumes+from+Google+Drive;🧠+NLP-Powered+Information+Extraction;📊+Export+Structured+Data+to+CSV;⚡+Education+%7C+Experience+%7C+Skills+%7C+Projects" alt="Typing SVG"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-00cfff?style=for-the-badge&logo=python&logoColor=white&labelColor=003366)
![NLP](https://img.shields.io/badge/NLP-spaCy-00cfff?style=for-the-badge&logo=spacy&logoColor=white&labelColor=003366)
![Google Drive](https://img.shields.io/badge/Google_Drive-API-00cfff?style=for-the-badge&logo=googledrive&logoColor=white&labelColor=003366)
![PDF](https://img.shields.io/badge/PDF-Parser-00cfff?style=for-the-badge&logo=adobeacrobatreader&logoColor=white&labelColor=003366)
![Status](https://img.shields.io/badge/STATUS-ACTIVE-00cfff?style=for-the-badge&logo=checkmarx&logoColor=white)

</div>

---

## 📌 About The Project

**Resume Analytics Platform** is an AI-powered tool that automatically fetches resumes from **Google Drive**, parses them using **NLP (spaCy)**, and extracts structured information like Education, Experience, Skills, and Projects — then exports everything to a **CSV file** for analytics.

```
📂 Google Drive Folder
        ↓
    PDF Resumes
        ↓
   NLP Parsing (spaCy)
        ↓
┌─────────────────────────┐
│  Education              │
│  Work Experience        │
│  Skills                 │
│  Projects               │
│  Named Entities (NER)   │
└─────────────────────────┘
        ↓
   📊 CSV Output
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 📥 **Google Drive Integration** | Auto-fetch resumes from a Drive folder |
| 📄 **PDF Parsing** | Extract raw text from PDF resumes |
| 🎓 **Education Extractor** | Detect degrees, colleges, years |
| 💼 **Experience Extractor** | Extract job roles, companies, durations |
| 🛠️ **Skill Extractor** | Identify technical and soft skills |
| 🚀 **Project Extractor** | Pull out project names and descriptions |
| 🧠 **NER Extractor** | Named Entity Recognition using spaCy |
| 📊 **CSV Export** | Save all extracted data in structured format |

---

## 🗂️ Project Structure

```
Resume Analytics Platform/
│
├── main.py                  # Entry point — runs the full pipeline
├── drive_manager.py         # Google Drive API — fetch resumes
├── pdf_parser.py            # Extract text from PDF files
├── resume_parser.py         # Orchestrates all extractors
├── education_extractor.py   # Extract education details
├── experience_extractor.py  # Extract work experience
├── skill_extractor.py       # Extract skills
├── project_extractor.py     # Extract projects
├── ner_extractor.py         # Named Entity Recognition (spaCy)
│
├── output/                  # Extracted CSV files saved here
│   └── extracted_data.csv
│
├── .env                     # 🔒 Secret keys (NOT uploaded to GitHub)
├── .env.example             # Template for environment variables
├── client_secrets.json      # 🔒 Google OAuth (NOT uploaded)
├── credentials.json         # 🔒 Google tokens (NOT uploaded)
├── .gitignore               # Ignores sensitive files
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/sourabhbagda24/Resume_analytics_platform.git
cd Resume_analytics_platform
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file in the root folder:
```
FOLDER_ID=your_google_drive_folder_id_here
```

> 💡 Refer to `.env.example` for the template

### 5. Setup Google Drive API

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Google Drive API**
- Download `client_secrets.json` and place it in the project root
- Run once to authenticate and generate `credentials.json`

### 6. Run the project
```bash
python main.py
```

---

## 📊 Output

After running, check the `output/` folder:

```
output/
└── extracted_data.csv    ← Structured resume data
```

Sample CSV columns:

| Name | Email | Education | Experience | Skills | Projects |
|------|-------|-----------|------------|--------|---------|
| Aarav Sharma | aarav@email.com | B.Tech CSE | Software Engineer @ XYZ | Python, ML | AI Chatbot |

---

## 🔒 Security

Sensitive files are **never uploaded** to GitHub:

```
✅ .env              → hidden via .gitignore
✅ config.py         → hidden via .gitignore
✅ client_secrets.json → hidden via .gitignore
✅ credentials.json  → hidden via .gitignore
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **spaCy** — NLP & Named Entity Recognition
- **pdfplumber** — PDF text extraction
- **Google Drive API** — Resume fetching
- **python-dotenv** — Environment variable management
- **pandas** — CSV export & data handling

---

## 🚀 Future Improvements

- [ ] Web dashboard (Streamlit/FastAPI)
- [ ] Resume scoring & ranking system
- [ ] ATS (Applicant Tracking System) integration
- [ ] Email alerts for new resumes
- [ ] Multi-language resume support

---

## 👨‍💻 Author

<div align="center">

**Sourabh Sharma**
AI Developer & ML Engineer | VIT Jaipur

[![LinkedIn](https://img.shields.io/badge/LinkedIn-003366?style=for-the-badge&logo=linkedin&logoColor=00cfff)](https://www.linkedin.com/in/sourabh-sharma-90758232b/)
[![GitHub](https://img.shields.io/badge/GitHub-003366?style=for-the-badge&logo=github&logoColor=00cfff)](https://github.com/sourabhbagda24)
[![Gmail](https://img.shields.io/badge/Gmail-003366?style=for-the-badge&logo=gmail&logoColor=00cfff)](mailto:sourabhbagda9@gmail.com)

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00cfff,50:003366,100:020b18&height=120&section=footer&animation=fadeIn"/>
</div>
