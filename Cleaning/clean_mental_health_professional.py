import pandas as pd

# Read CSV
df = pd.read_csv("Access_to_Care_Dataset.csv")

# Filter rows
filtered_df = df[
    (df["TOPIC"] == "Counseled by a mental health professional") &
    (df["GROUP"].isin([
        "Health insurance coverage: Younger than 65 years",
        "Health insurance coverage: 65 years and older"
    ]))
]

# Save new CSV
filtered_df.to_csv(
    "Counseled_Mental_Health_By_Insurance.csv",
    index=False
)

print("Done! File saved as Counseled_Mental_Health_By_Insurance.csv")