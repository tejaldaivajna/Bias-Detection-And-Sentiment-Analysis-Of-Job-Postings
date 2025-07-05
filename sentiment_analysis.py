import os
import pandas as pd
import hashlib
import json
from groq import Groq
from tqdm import tqdm  # progress bar

# Set up Groq client
client = Groq(api_key="your-groq-api-key") # Insert your Groq API key here

# Load job descriptions
df = pd.read_csv("flagged_job_descriptions.csv")

# Cache setup
cache_path = "groq_sentiment_cache.json"
if os.path.exists(cache_path):
    with open(cache_path, "r") as f:
        sentiment_cache = json.load(f)
else:
    sentiment_cache = {}

# Hash helper
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Main sentiment function using Groq SDK
def get_groq_sentiment(text):
    if not isinstance(text, str) or not text.strip():
        return "Unknown"

    text_hash = hash_text(text)

    if text_hash in sentiment_cache:
        return sentiment_cache[text_hash]

    prompt = f"""
        You are a sentiment analysis assistant. Analyze the following job description and classify its overall tone as one of:
        - Positive (if it promotes good work culture and work-life balance)
        - Neutral
        - Negative (if it contains language that promotes overwork or intense pressure)

        Respond with only one of these labels: Positive, Neutral, Negative.

        Text:
        \"\"\"
        {text}
        \"\"\"
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        label = response.choices[0].message.content.strip()
        sentiment_cache[text_hash] = label
        return label

    except Exception as e:
        print("Groq API error:", e)
        return "Error"

# Apply sentiment with progress bar
tqdm.pandas()
df["Sentiment"] = df["Description"].progress_apply(get_groq_sentiment)

# Save updated cache
with open(cache_path, "w") as f:
    json.dump(sentiment_cache, f, indent=2)

# Save final CSV
df.to_csv("groq_sentiment_job_descriptions.csv", index=False)
print("File saved as 'groq_sentiment_job_descriptions.csv'")