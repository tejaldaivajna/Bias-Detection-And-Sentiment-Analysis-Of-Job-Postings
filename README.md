# 🧠 Bias & Sentiment Audit of Job Postings

🔗 **View the Interactive Dashboard on Tableau**  
[Click here](https://public.tableau.com/views/BiasDetectionandSentimentAnalysisofJobPostings/BiasDashboard?:language=en-GB&:sid=&:display_count=n&:origin=viz_share_link)

---

## 📌 Overview

This project uses **Natural Language Processing (NLP)** to audit over **300 job postings** for **Data Analyst** and **Data Scientist** roles across India — all scraped directly from **Indeed**.

It aims to help **HR teams and recruiters**:
- Detect **biased or exclusionary language** that could affect applicant diversity.
- Understand the **tone** of job descriptions (positive, neutral, or negative).
- Visualize geographic and company-level trends in bias and sentiment.

---

## 🧰 Tech Stack
- **Python**: Scraping, preprocessing, NLP analysis
- **spaCy**: Tokenization and lemmatization
- **Custom Bias Dictionary**: For flagging gender-coded and pressure language
- **Groq (LLaMA-3.3-70B)**: For sentiment classification via API
- **Tableau**: For interactive data visualization

---

## 🧩 How It Works

### 1. **Scraping** (`scraper.py`)
Scrapes job descriptions for Data Scientist/Analyst roles in India from Indeed using Selenium and Undetected ChromeDriver.

### 2. **Bias Detection** (`bias_detection.py`)
- Cleans and lemmatizes the job text using spaCy
- Flags biased terms from a curated dictionary
- Appends flagged terms to each record

### 3. **Sentiment Analysis** (`sentiment_analysis.py`)
- Uses Groq's LLaMA-3.3-70B model via API
- Classifies job descriptions as **Positive**, **Neutral**, or **Negative**
- Caches results to avoid redundant API calls

### 4. **Processing** (`processing.py`)
- Merges bias and sentiment outputs
- Generates supporting columns such as city and explodes flagged terms for visualization
- Prepares final structured CSV for visualization

### 5. **Visualization** (`Bias Detection and Sentiment Analysis of Job Postings.twbx`)
The processed dataset is visualized in **Tableau** to uncover trends across locations, companies, and job tone.

---
