import pandas as pd
import sqlite3

# Load the original CSV
df = pd.read_csv("survey_responses.csv")

# Rename columns
df.columns = [
    "timestamp",
    "campus",
    "school_year",
    "occasion",
    "purchase_location",
    "buy_motivation",
    "brand_vibe"
]

# Optional: preview cleaned data
print(df.head())

# Connect to SQLite and store the data
conn = sqlite3.connect("redbull_survey.db")
df.to_sql("survey_responses", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("✅ Survey data saved to redbull_survey.db in table 'survey_responses'")
