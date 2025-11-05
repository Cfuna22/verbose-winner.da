import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

# Display first few rows
print(df.head())

# Shape and info
print(df.shape)
print(df.info())

# Quick stats
print(df.describe())
