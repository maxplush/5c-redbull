import sqlite3
import pandas as pd
from collections import Counter
import re
from textblob import TextBlob

# Connect to the database
conn = sqlite3.connect("redbull_survey.db")

# Define queries
queries = {
    "Occasion Breakdown": """
    SELECT
        occasion AS response,
        COUNT(*) AS count,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM survey_responses), 1) AS percentage
    FROM survey_responses
    GROUP BY response
    ORDER BY count DESC;
    """,
    "Purchase Location": """
    SELECT
        purchase_location AS response,
        COUNT(*) AS count,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM survey_responses), 1) AS percentage
    FROM survey_responses
    GROUP BY response
    ORDER BY count DESC;
    """,
    "Motivation to Buy": """
    SELECT
        buy_motivation AS response,
        COUNT(*) AS count,
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM survey_responses), 1) AS percentage
    FROM survey_responses
    GROUP BY response
    ORDER BY count DESC;
    """
}

# Initialize output summary
summary = "# 🧠 Red Bull x 5C Survey Summary\n\n"

# Run each SQL query and format results
for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    summary += f"## 📊 {name}\n\n"
    for _, row in df.iterrows():
        summary += f"- **{row['response']}**: {row['count']} responses ({row['percentage']}%)\n"
    summary += "\n"

# === Brand Vibe Analysis ===
summary += "## 🎨 Brand Vibe Word Frequency & Sentiment\n\n"

# Load non-null brand vibe responses
df_vibe = pd.read_sql_query("SELECT brand_vibe FROM survey_responses WHERE brand_vibe IS NOT NULL", conn)
conn.close()

# Tokenize and count words
all_words = []
for text in df_vibe['brand_vibe']:
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    all_words.extend(words)

word_freq = Counter(all_words)
top_words = word_freq.most_common(10)

summary += "### 🔠 Top 10 Words Used\n\n"
for word, freq in top_words:
    summary += f"- {word}: {freq} mentions\n"

# Sentiment analysis
sentiments = df_vibe['brand_vibe'].apply(lambda x: TextBlob(x).sentiment.polarity)

def categorize(p):
    if p > 0.2:
        return "Positive"
    elif p < -0.2:
        return "Negative"
    else:
        return "Neutral"

sentiment_labels = sentiments.apply(categorize)
sentiment_summary = sentiment_labels.value_counts(normalize=True).round(2) * 100

summary += "\n### 😊 Sentiment Breakdown\n\n"
for sentiment, pct in sentiment_summary.items():
    summary += f"- {sentiment}: {pct}%\n"

# Write the report to a file
with open("redbull_summary.txt", "w") as f:
    f.write(summary)

print("✅ Summary written to redbull_summary.txt")