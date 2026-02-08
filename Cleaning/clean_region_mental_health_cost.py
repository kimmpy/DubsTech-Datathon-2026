import pandas as pd

# Read CSV
df = pd.read_csv("../Data/Access_to_Care_Dataset.csv")

# Filter rows
filtered_df = df[
    (df["TOPIC"] == "Did not get needed mental health care due to cost") &
    (df["GROUP"].isin([
        "Region"
    ]))
]

# Save new CSV
filtered_df.to_csv(
    "Did_Not_Get_Mental_Health_Care_By_Region.csv",
    index=False
)

print("Done! File saved as Did_Not_Get_Mental_Health_Care_By_Region.csv")