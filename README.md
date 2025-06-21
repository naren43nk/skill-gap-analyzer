# 📊 UK Data Job Skill Gap Analyzer

An interactive Streamlit dashboard that visualizes in-demand skills across various data roles in the UK job market using real-time data from the Adzuna Job Search API.

![Streamlit Banner](https://user-images.githubusercontent.com/your-banner-image-here)

---

## 🚀 Live Demo

🔗 **[Click to View the App →](https://naren43nk-skill-gap-analyzer.streamlit.app)**  
*(Public Streamlit Cloud deployment – updated weekly)*

---

## 🎯 Project Overview

The **Skill Gap Analyzer** helps:
- 🎓 Data science & engineering students identify in-demand UK skills
- 💼 Job seekers target specific cities and job roles
- 🧠 Recruiters analyze skill distribution and hiring trends

---

## 🔍 Features

- 🔽 **Dropdown filters** for job role and city  
- 📊 **Top 20 skills bar chart** by role or city  
- 📈 **Skill trends over time** using scrape dates  
- 🗃️ Powered by **Adzuna's public job API**  
- 🌐 Fully deployed and open source

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core logic & scripting |
| 🧠 spaCy + PhraseMatcher | NLP-based skill extraction |
| 📊 Pandas | Data cleaning and analysis |
| 🧮 Streamlit | Dashboard and frontend |
| 🗃️ Adzuna API | UK job postings |
| ☁️ Streamlit Cloud | App hosting |
| 🔐 dotenv / secrets.toml | Secure API key handling |

---

## 🧪 Data Flow

Adzuna Job API →
Raw job descriptions →
spaCy Skill Extraction →
Grouped by role, city, date →
Streamlit Dashboard


🗂️ Folder Structure

skill-gap-analyzer/
├── app.py                      # Streamlit app
├── data/                       # Processed CSVs (skill trends, etc.)
├── utils/
│   ├── scraper.py              # Scrapes jobs from Adzuna API
│   ├── skill_extractor.py      # NLP skill extraction
│   └── skill_analysis_extended.py
├── .streamlit/secrets.toml     # API keys (cloud only)
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How to Run Locally

# 1. Clone the repo
git clone git@github.com:naren43nk/skill-gap-analyzer.git
cd skill-gap-analyzer

# 2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Adzuna API keys to `.env`
echo "ADZUNA_APP_ID=your_id" > .env
echo "ADZUNA_APP_KEY=your_key" >> .env

# 5. Run the Streamlit app
streamlit run app.py

📬 Contact
Narendran Mohan
🎓 MSc Data Science – University of Surrey
📧 narenkarthi29776@gmail.com
🔗 LinkedIn | GitHub

⭐ Acknowledgements
Adzuna Developer API
Streamlit
spaCy NLP Toolkit


