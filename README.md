# 🧠 Bias & Sentiment Audit of Job Postings

🔗 **View the Interactive Dashboard on Tableau**  
[👉 Click here to explore the dashboard]([https://public.tableau.com/app/profile/your-link-here](https://public.tableau.com/views/BiasDetectionandSentimentAnalysisofJobPostings/BiasDashboard?:language=en-GB&:sid=&:display_count=n&:origin=viz_share_link))

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

### 2. **Processing & Bias Detection** (`processing.py` + `bias_detection.py`)
- Cleans and lemmatizes the job text
- Flags biased terms from a curated dictionary
- Outputs job posts with identified bias terms

### 3. **Sentiment Analysis** (`sentiment_analysis.py`)
- Uses Groq's LLaMA-3.3-70B model via API
- Classifies job descriptions as **Positive**, **Neutral**, or **Negative**
- Caches results to avoid reprocessing

### 4. **Visualization**
Data is exported to CSV and visualized in Tableau:
- **Geographic Bias Rate Map**
- **Sentiment Distribution**
- **Company-wise Bias and Sentiment**
- **Flagged Terms Word Cloud**

---
