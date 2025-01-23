# Banking Disinformation Analysis

<br>

## 📖 Overview
This project focuses on analyzing disinformation narratives in the banking sector, leveraging data analysis to process large datasets and uncover patterns of toxicity, claim matching, and suspicious behavior. It aligns with business needs by providing clear, actionable insights through a dashboard and identifying automation opportunities to enhance decision-making for stakeholders.

<br>

## 📂 Project Structure

- auxiliar
  - trueflag_icon.png
  - trueflag_logo.png
- data
  - raw *[input files should be stored here]*
  - processed
- etl_processing.py
- requirements.txt
- README.md

4 directories, 5 files

<br>

---

<br>

## 🎯 General Considerations

**Key attributes used in analysis to identify suspicious content**:
   - **Toxicity Ratio**: Average of messages identified as toxic. A reference value of 40% (dataset average) is considered.
   - **Claim Matching Ratio**: Average of messages matched with a published fact-check. A reference value of 40% (dataset average) is considered.
   - **Potential Bot Users**: Users with more than 14 messages per week in average, and a toxicity ratio above the network reference value (40%).
   - **Object-Directed Messages**: Content explicitly targeting individuals or entities.
       
<br>

## 📊 Dashboard Analytics

The Power BI dashboard (that can be found [here](https://app.powerbi.com/view?r=eyJrIjoiM2I2NDExYjQtMGJhNy00YjgyLTg1N2UtMGZjODE2YWFjNzViIiwidCI6ImU3ZjUzZjNmLTYzNmItNDNhZC04MDdlLTU3Yzk2NmZmN2RiOCIsImMiOjh9)) is the deliverable used to visualize the extracted analyses. Each view there contained is described below:

### Views and Analysis

#### 1. General Context View

- **Purpose**: To contextualize the general state of the network. Understand user behavior within the network, as well as the most representative general topics.
- **Key Metrics**:
  - Total number of messages and users analyzed.
  - Claim matching and toxicity ratios per message.
  - Sentiment analysis of the messages.
  - Overview of users and types of attacks within the network.

#### 2. Bank Narratives View

- **Purpose**: Analysis of specific narratives about the banking sector and their characteristics. Contextualize these narratives concerning the existing network behavior.
- **Key Metrics**:
  - Main KPIs in the banking sector versus the overall network.
  - Analysis of main narratives by ratios, whether object-directed and message volume.
  - Identification of suspicious behavior patterns by weekday and timeslot.
  - Key active users within the banking sector narratives.

#### 3. Users in Network View

- **Purpose**: Analysis of user behavior within the network, identifying patterns and suspicious content creators.
- **Key Metrics**:
  - Main KPIs by user(s) versus the overall network.
  - Identification of trends and user clusters based on claim matching, toxicity, and bot likelihood.
  - Detailed user behavior and their attributes.

<br>

---

<br>

## 🎥 Demo videos

- **Video 1 - General Context View**
  https://www.loom.com/share/dcb27c59e7104de1bef5520883a8e91a?sid=4373e5d8-c50b-4ce1-8561-f9ffe1544761

 - **Video 2 - Bank Narratives View (Part 1)**
   https://www.loom.com/share/d636b9d3cc2b4d63a208fd69c8b5d124?sid=106ca9f2-1eb9-4e01-9a78-20b3b7bbac5f

 - **Video 3 - Bank Narratives View (Part 2)**
   https://www.loom.com/share/696070d8229d4b8baf13a45eb3b27938?sid=6c4934cf-f5f6-4d38-baea-a253a7a3412d

 - **Video 4 - Users in Network View**
   https://www.loom.com/share/a853ec5d0b8d4661bd4c2733310646b9?sid=84400977-a253-41f1-8846-f43ffa39ee04
<br>
---
<br>

## 🚀 Deploy Instructions

### Step 1: Clone repository
```bash
git clone https://github.com/yourusername/banking-disinformation-analysis.git
cd banking-disinformation-analysis
```

### Step 2: Create virtual environment and install dependencies
```bash
python -m venv disinformation_narrative_storytelling
disinformation_narrative_storytelling\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Run data processing script
Replace `<script_path>` with the correct path to the processing script:
```bash
python <script_path>
```

### Step 4: Update Power BI 'Source path file'
Modify the `Source path file` parameter in Power BI Desktop to point to the `data` folder on the deployment system.

<br>
---
<br>

## 🛠 Tools and Technologies
- **Data Processing**:
  - Python (pandas, os)
- **Visualization**:
  - Power BI

<br>

## 🔗 Resources
- [Shared public link of Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiM2I2NDExYjQtMGJhNy00YjgyLTg1N2UtMGZjODE2YWFjNzViIiwidCI6ImU3ZjUzZjNmLTYzNmItNDNhZC04MDdlLTU3Yzk2NmZmN2RiOCIsImMiOjh9)


