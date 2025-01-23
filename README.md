# Banking Disinformation Analysis

## 📖 Overview
This project aims to analyze disinformation narratives about the banking sector during October. By utilizing datasets enriched with toxicity classifications, claim matching, and topic modeling, the analysis identifies suspicious and potentially malicious content. The findings are visualized through a series of dashboards to support storytelling and client decision-making.


## 📂 Project Structure

- auxiliar
  - trueflag_icon.png
  - trueflag_logo.png
- data
  - raw *// input files should be stored here*
  - processed
- etl_processing.py
- requirements.txt
- README.md


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

## 📊 Dashboard Analytics

Vídeo 1: https://www.loom.com/share/8d27bda72d384f0da6ed225d7109b696?sid=8b4d5016-8d70-4cf6-8130-e972b241a3fb
Vídeo 2.1: https://www.loom.com/share/d636b9d3cc2b4d63a208fd69c8b5d124?sid=106ca9f2-1eb9-4e01-9a78-20b3b7bbac5f
Vídeo 2.2: https://www.loom.com/share/696070d8229d4b8baf13a45eb3b27938?sid=6c4934cf-f5f6-4d38-baea-a253a7a3412d
Vídeo 3: https://www.loom.com/share/a853ec5d0b8d4661bd4c2733310646b9?sid=84400977-a253-41f1-8846-f43ffa39ee04

The Power BI dashboard is designed to provide insights into disinformation narratives related to the banking sector. Below is a description of each view and its functionality:

0. Consideraciones generales
    - **Atributos de estudio para identificar contenido sospechoso**:
      - Ratio de toxicidad. Threshold value:
      - Ratio de claim matching. Treshold value:
      - User is potential bot. Computed as:
      - Message is object directed.  

1. **General context view**:
   - **Purpose**: Contextualizar estado general de la red. Entender cómo es el comportamiento de los usuarios en la red, así como de los temas generales más representativos.
   - **Key Metrics**:
     - Total number of messages, usuarios analyzed.
     - Claim matching y Toxicity ratios por mensaje.
     - Análisis de sentimientos de los mensajes.
    
2. **Bank narratives view**:
  - **Purpose**: Analizar narrativas sobre el sector bancario, en cuanto a . Contextualizar estado general de la red. Entender cómo es el comportamiento de los usuarios en la red, así como de los temas generales más representativos.
   - **Key Metrics**:
     - Total number of messages, usuarios analyzed.
     - Claim matching y Toxicity ratios por mensaje.
     - Análisis de sentimientos de los mensajes.

3. **Users in network view**
   - **Purpose**: Contextualizar estado general de la red. Entender cómo es el comportamiento de los usuarios en la red, así como de los temas generales más representativos.
   - **Key Metrics**:
     - Total number of messages, usuarios analyzed.
     - Claim matching y Toxicity ratios por mensaje.
     - Análisis de sentimientos de los mensajes.
    
Consideraciones generales
    - **Atributos de estudio para identificar contenido sospechoso**:
      - Ratio de toxicidad. Threshold value:
      Ratio de claim matching. Treshold value:
      User is potential bot. Computed as:
      Message is object directed.  

1. Valores de threshold para id
    
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
