# 🧠 AI Data Storyteller

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/streamlit-v1.24-orange)](https://streamlit.io/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**AI Data Storyteller** is a Streamlit app that lets you upload a CSV dataset, explore key statistics, visualize patterns, generate AI-powered insights, and download a professional PDF report — all in one place.

---
## 🚀 Features

* **Quick Data Summary:** View column types, missing values, unique counts, and first rows. 
* **Interactive Visualizations:**

  * Numeric columns → histograms & KDE
  * Categorical columns → bar charts (up to 15 unique values)
  * Correlation heatmaps for numeric data
* **AI-Powered Executive Summary:** Automatic EDA insights using GROQ API.
* **PDF Report Generation:** Includes AI summary + visualizations, ready to download.

---

## ⚡ Installation

```bash
git clone <repo-url>
cd <repo-folder>
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

> **Optional:** Set your GROQ API key for AI insights:

```bash
export GROQ_API_KEY="your_api_key"  # Linux/Mac
set GROQ_API_KEY="your_api_key"     # Windows
```

---

## 🛠 Usage

```bash
streamlit run app.py
```

1. Upload your CSV file.
2. Explore data summaries and visualizations.
3. Generate AI-powered executive summary.
4. Download the PDF report.

---

## 📊 Notes

* Only first 3 numeric and categorical columns are visualized.
* Categorical columns with >20 unique values are skipped for bar charts.
* Temporary images are deleted after PDF generation.

---

## 📂 Dependencies

* Python ≥ 3.8
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [FPDF](https://pyfpdf.github.io/fpdf2/)
* [LangChain](https://www.langchain.com/) (for GROQ integration)

---

## 📸 Screenshots

Homepage view:  
![Homepage](screenshots/homepage.png)

Visualizations example:  
![Charts](screenshots/visyalizations-heatmap.png)
![Charts](screenshots/visyalizations-plots.png)


