

---

## ⚙️ Workflow

### 1. Data Ingestion
- **Input**: Raw CSV files located in `data/` directory.
- **Validation**:
  - Files are checked for structure, missing values, and required columns.
  - Anomalies are logged in `logs/`.

### 2. Data Processing
- **Script**: `scripts/process_data.py`
- **Transformations**:
  - Clean null values.
  - Standardize date and numeric formats.
  - Apply business rules (e.g., filtering rows based on conditions).
- **Output**: Processed CSV files saved in `processed_data/`.

### 3. Integration with Power BI
- **Steps**:
  1. Import processed files from `processed_data/` into Power BI.
  2. Use `PowerBI_Report.pbit` as the report template.
- **Key Visuals**:
  - Summary statistics.
  - Trends over time.
  - Custom KPIs.

---

## 📋 Prerequisites
1. **Python Environment**:
   - Python 3.8+
   - Required packages:
     ```
     pandas
     numpy
     logging
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
2. **Power BI Desktop**:
   - [Download here](https://powerbi.microsoft.com/desktop/).

---

## 🚀 Setup and Usage

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
