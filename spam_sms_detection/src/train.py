import pandas as pd

# Load dataset
df = pd.read_csv("data/spam.csv", encoding="latin-1")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())