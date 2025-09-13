# 🧠 AI Data Storyteller

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/streamlit-v1.24-orange)](https://streamlit.io/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**AI Data Storyteller** is an intuitive Streamlit web application that allows users to upload CSV datasets, perform exploratory data analysis (EDA), visualize key patterns, generate AI-powered insights, and download a professional PDF report — all without writing a single line of code.

---

## 🚀 Features

* **Quick Data Summary:** Automatically shows column types, missing values, unique counts, and the first few rows of your dataset.
* **Interactive Visualizations:**

  * Numeric columns → histograms & KDE
  * Categorical columns → bar charts (up to 15 unique values)
  * Correlation heatmaps for numeric columns
* **AI-Powered Executive Summary:** Generates EDA insights using the GROQ API and LangChain.
* **PDF Report Generation:** Combines visualizations and AI insights into a downloadable PDF.

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Set your GROQ API key to enable AI insights:

```bash
export GROQ_API_KEY="your_api_key"  # Linux/Mac
set GROQ_API_KEY="your_api_key"     # Windows
```

---

## 🛠 Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload a CSV file.
3. Explore data summaries, numeric and categorical visualizations.
4. Generate AI-powered executive summary.
5. Download the PDF report with insights and charts.

---

## 📊 Notes

* Only the first 3 numeric and categorical columns are visualized for clarity.
* Categorical columns with more than 20 unique values are skipped for bar charts.
* Temporary images used in PDF generation are automatically deleted.

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

---

## 📝 License

MIT License — free for educational and commercial use.
