import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("redbull_survey.db")

# Define queries
queries = {
    "Occasion Breakdown": """
        SELECT occasion, COUNT(*) AS count
        FROM survey_responses
        GROUP BY occasion
        ORDER BY count DESC;
    """,
    "Purchase Location": """
        SELECT purchase_location, COUNT(*) AS count
        FROM survey_responses
        GROUP BY purchase_location
        ORDER BY count DESC;
    """,
    "Motivation to Buy": """
        SELECT buy_motivation, COUNT(*) AS count
        FROM survey_responses
        GROUP BY buy_motivation
        ORDER BY count DESC;
    """,
    "Brand Vibes (Top Mentions)": """
        SELECT brand_vibe, COUNT(*) AS count
        FROM survey_responses
        GROUP BY brand_vibe
        ORDER BY count DESC
        LIMIT 10;
    """
}

# Run and print results
for name, query in queries.items():
    print(f"\n📊 {name}")
    df = pd.read_sql_query(query, conn)
    print(df)

conn.close()
