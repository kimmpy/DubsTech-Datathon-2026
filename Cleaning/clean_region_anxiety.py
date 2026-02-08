import pandas as pd

# Read CSV
df = pd.read_csv("../Data/Access_to_Care_Dataset.csv")

# Filter rows
filtered_df = df[
    (df["TOPIC"] == "Regularly had feelings of worry, nervousness, or anxiety") &
    (df["GROUP"].isin([
        "Region"
    ]))
]

# Save new CSV
filtered_df.to_csv(
    "Rate_Of_Anxiety_By_Region.csv",
    index=False
)

print("Done! File saved as Rate_Of_Anxiety_By_Region.csv")