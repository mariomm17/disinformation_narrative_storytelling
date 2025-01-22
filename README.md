# Banking Disinformation Analysis

## 📖 Overview
This project aims to analyze disinformation narratives about the banking sector during October. By utilizing datasets enriched with toxicity classifications, claim matching, and topic modeling, the analysis identifies suspicious and potentially malicious content. The findings are visualized through a series of dashboards to support storytelling and client decision-making.

---

## 📂 Project Structure
├── auxiliar
│   ├── trueflag_icon.png
│   └── trueflag_logo.png
├── data
│   ├── raw
│	│	└── {Here should input files be stored}
│   └── processed
├── etl_processing.py
├── requirements.txt
└── README.md

4 directories, 5 files

---

## 🎯 Objectives
1. Identify narratives with:
   - High toxicity levels.
   - Targeted attacks on banks, institutions, or products.
   - Connections to verified claim reviews (fact-checking).
   - Malicious intent based on manual inspection.
2. Provide actionable insights through visual storytelling and comparative panels.

---

## ⚙️ Workflow

### 1. Data Ingestion
- Load datasets into a structured format (e.g., SQL database or Pandas DataFrame).
- Log missing or incomplete data for debugging.

### 2. Data Transformation
- Merge datasets using `content_id` as the key.
- Enrich data with computed metrics:
  - Toxicity score distribution.
  - Frequency of fact-check matches.
  - Clusters most associated with banking disinformation.

### 3. Analysis
- Identify narratives matching suspicious criteria:
  - High toxicity + targeted attack.
  - Fact-check matches indicating disinformation.
- Generate metrics for:
  - Volume and frequency of toxic messages.
  - Impacted brands or institutions.
  - Cluster summaries.

### 4. Visualization
- **Dashboard Components**:
  - **Volume Analysis**: General, banking-specific, and attacker-specific data comparisons.
  - **Suspicious Narratives**: Toxicity levels, targeted attacks, and fact-check connections.
  - **Time Trends**: Activity over October.
  - **Brand Impact**: Most affected entities.
- Interactive filters for:
  - Date range.
  - Narrative type (e.g., toxic, targeted attack).
  - Keywords.

---

## 🛠 Tools and Technologies
- **Data Processing**:
  - Python (pandas, numpy, SQLAlchemy, matplotlib, seaborn)
- **Visualization**:
  - Power BI (pbix file included in `dashboards/` folder)
- **Database**:
  - SQLite (or preferred OLAP system for scalability)
- **Logging**:
  - Python logging module

---

## 🔗 Resources
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)
- [Python pandas Documentation](https://pandas.pydata.org/docs/)
- Dataset description included in the "Task Definition".

---

## 🚀 Setup Instructions

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/banking-disinformation-analysis.git
cd banking-disinformation-analysis
