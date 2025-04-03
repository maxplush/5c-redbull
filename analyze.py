import sqlite3
import pandas as pd

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

# Run and print results
for name, query in queries.items():
    print(f"\n📊 {name}")
    df = pd.read_sql_query(query, conn)
    print(df)

conn.close()
