import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

# -------------------------------
# Page Setup and Introduction
# -------------------------------
st.set_page_config(page_title="AI Data Storyteller", layout="wide")
st.title("AI Data Storyteller")

st.markdown("""
Upload your CSV dataset to quickly explore data structure, key statistics, and visualize important patterns.  
Use the AI-powered summary to get concise insights and download a comprehensive report for your records.  
""")

# -------------------------------
# Upload CSV File
# -------------------------------
file = st.file_uploader("Upload your CSV file", type=["csv"])
if not file:
    st.info("Please upload a CSV file to proceed.")
    st.stop()

try:
    df = pd.read_csv(file)
    if df.empty:
        st.error("The uploaded CSV file is empty. Please upload a valid dataset.")
        st.stop()
except Exception as e:
    st.error(f"Error loading CSV file: {e}")
    st.stop()

st.success(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
st.dataframe(df.head(8))

# -------------------------------
# Column Overview
# -------------------------------
st.header("Data Summary")
col_info = pd.DataFrame({
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum(),
    "Unique Values": df.nunique()
})
st.dataframe(col_info)

# -------------------------------
# Prepare Columns for Visualization
# -------------------------------
numeric_columns = df.select_dtypes(include="number").columns.tolist()
categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

# -------------------------------
# Visualizations
# -------------------------------
st.header("Data Visualizations")
st.subheader("Numeric Columns Distribution")

num_cols_to_show = numeric_columns[:3]
cols = st.columns(3)
for idx, col in enumerate(num_cols_to_show):
    with cols[idx]:
        st.markdown(f"**Distribution of `{col}`**")
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color="#1f77b4")
        plt.tight_layout()
        st.pyplot(fig)

st.subheader("Categorical Columns Value Counts")
cat_cols_to_show = [c for c in categorical_columns if df[c].nunique() < 20][:3]
cols = st.columns(3)
for idx, col in enumerate(cat_cols_to_show):
    with cols[idx]:
        st.markdown(f"**Value counts for `{col}`**")
        counts = df[col].value_counts().nlargest(15)
        fig, ax = plt.subplots(figsize=(5, 3))
        counts.plot.bar(ax=ax, color="#ff7f0e")
        ax.set_xticklabels(counts.index, rotation=45, ha="right", fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)

if len(numeric_columns) > 1:
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(max(6, len(numeric_columns) * 1.1), 5))
    corr = df[numeric_columns].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax, annot_kws={"size": 8})
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.info("Not enough numeric columns for correlation heatmap.")

# -------------------------------
# AI Executive Summary
# -------------------------------
st.header("Executive Summary")
api_key = os.getenv("GROQ_API_KEY")
report_text = ""

if not api_key:
    st.warning("Set the GROQ_API_KEY environment variable to enable AI insights.")
else:
    from langchain_groq import ChatGroq
    from langchain.prompts import PromptTemplate

    prompt = PromptTemplate(
        input_variables=["summary", "sample"],
        template="""
You are a skilled data scientist performing a complete exploratory data analysis on the given dataset.  
Please generate a thorough summarized report that includes key statistics, important patterns, data quality observations, actionable insights, and a clear overall conclusion.
Dataset summary:
{summary}

Sample of Data:
{sample}
"""
    ).format(summary=df.describe(include="all").to_json(), sample=df.head(5).to_json())

    chat = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama-3.3-70b-versatile")
    resp = chat.invoke(prompt)
    report_text = getattr(resp, "content", getattr(resp, "text", "No report generated."))
    st.markdown(report_text)

# -------------------------------
# Generate PDF Report
# -------------------------------
def save_figures_for_pdf(df, numeric_cols, categorical_cols):
    plot_paths = []
    for col in numeric_cols[:3]:
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        ax.set_title(col)
        plt.tight_layout()
        path = f"{col}_hist.png"
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        plot_paths.append(path)
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(max(6, len(numeric_cols) * 1.1), 5))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax, annot_kws={"size": 8})
        plt.xticks(rotation=45, ha="right", fontsize=8)
        plt.tight_layout()
        path = "correlation_heatmap.png"
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        plot_paths.append(path)
    for col in [c for c in categorical_cols if df[c].nunique() < 20][:1]:
        counts = df[col].value_counts().nlargest(15)
        fig, ax = plt.subplots(figsize=(5, 3))
        counts.plot.bar(ax=ax)
        ax.set_title(col)
        ax.set_xticklabels(counts.index, rotation=45, ha="right", fontsize=9)
        plt.tight_layout()
        path = f"{col}_bar.png"
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        plot_paths.append(path)
    return plot_paths

plot_paths = save_figures_for_pdf(df, numeric_columns, categorical_columns)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.multi_cell(0, 10, "AI Data Storyteller Report", 0, "C")
pdf.ln(5)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, report_text)
pdf.ln(10)

y_pos = pdf.get_y()
img_w, img_h = 80, 60

for path in plot_paths:
    if y_pos + img_h > pdf.page_break_trigger:
        pdf.add_page()
        y_pos = pdf.get_y()
    pdf.image(path, x=15, y=y_pos, w=img_w)
    y_pos += img_h + 10

pdf_file = "Executive_Report.pdf"
pdf.output(pdf_file)

for path in plot_paths:
    if os.path.exists(path):
        os.remove(path)

st.download_button("⬇️ Download PDF Report", open(pdf_file, "rb"), file_name=pdf_file, mime="application/pdf")
st.success("Report generation complete! Download your executive summary.")
