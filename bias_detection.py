import pandas as pd
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load scraped job descriptions
df = pd.read_csv("job_descriptions.csv")

# Bias dictionary
bias_dict = {
    # Masculine-coded
    "aggressive": "assertive",
    "dominant": "confident",
    "driven": "motivated",
    "competitive": "collaborative",
    "decisive": "clear-thinking",
    "rockstar": "expert",
    "ninja": "specialist",
    "guru": "professional",
    "fearless": "resilient",
    "headstrong": "determined",
    "ambitious": "goal-oriented",

    # Feminine-coded
    "supportive": "collaborative",
    "nurturing": "encouraging",
    "understanding": "empathetic",
    "emotional": "self-aware",
    "sensitive": "mindful",
    "dependable": "reliable",
    "loyal": "dedicated",

    # Exclusive / Gender-biased
    "manpower": "workforce",
    "female-only": "open to all genders",
    "ideal for women": "welcoming to all applicants",
    "she": "they",
    "he": "they",
    "his": "their",
    "her": "their",

    # Burnout / Pressure terms
    "fast-paced environment": "dynamic environment",
    "work hard play hard": None,
    "thick-skinned": None,
    "must handle pressure": None,
    "grind": None,
    "always available": None,

    # Buzzwords
    # "synergy": "collaboration",
    # "go-getter": "self-motivated",
    # "outside the box": "creative",
    # "hit the ground running": "proactive start",
}

# Normalize to lowercase for matching
bias_terms = set(bias_dict.keys())

person_keywords = {"candidate", "person", "employee", "individual", "team member", "leader", "applicant"}

def flag_bias(text):
    if pd.isna(text):
        return ""

    doc = nlp(text)
    tokens = list(doc)
    found = set()

    for i, token in enumerate(tokens):
        lemma = token.lemma_.lower()

        if lemma not in bias_terms:
            continue

        # Custom rule for "understanding"
        if lemma == "understanding":
            if token.pos_ == "ADJ":
                found.add(lemma)
            else:
                # Check if "understanding" is near a person-related word (it has to be an adjective for it to be a biased word)
                context_window = tokens[max(0, i-4): i+5]
                context_lemmas = {t.lemma_.lower() for t in context_window}
                if context_lemmas.intersection(person_keywords):
                    found.add(lemma)

        else:
            found.add(lemma)

    return ", ".join(sorted(found))

# Add 'Flagged Terms' column
df["Flagged Terms"] = df["Description"].apply(flag_bias)

# Save to new file
df.to_csv("flagged_job_descriptions.csv", index=False)
print("Saved new CSV with 'Flagged Terms' column.")