import pandas as pd

df = pd.read_csv('groq_sentiment_job_descriptions.csv')
df = df.drop('Unnamed: 0', axis=1)

def extract_city(location):
    if pd.isna(location):
        return None

    location = location.strip()

    if location.startswith('Hybrid work in '):
        location = location.replace('Hybrid work in ', '')

    if 'Remote' in location:
        return 'Remote'

    parts = [part.strip() for part in location.split(',')]
    if len(parts) == 1:
        return parts[0]
    else:
        return parts[-2]  # Second last part is usually the city

df['City'] = df['Location'].apply(extract_city)

loc_index = df.columns.get_loc('Location')
city_col = df.pop('City')
df.insert(loc_index + 1, 'City', city_col)

df.to_csv('final_dataset.csv', index=False)

# Saving exploded flagged terms separately for Tableau word cloud
exploded = df.dropna(subset=["Flagged Terms"]).copy()
exploded["Flagged Terms"] = exploded["Flagged Terms"].str.split(",\s*")
exploded = exploded.explode("Flagged Terms")
exploded["Flagged Terms"] = exploded["Flagged Terms"].str.strip()  # remove whitespace
exploded.to_csv("wordcloud.csv", index=False)
print("Saved exploded CSV as 'wordcloud.csv'")