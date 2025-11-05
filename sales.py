import pandas as pd

# create DataFrames
data = {
    'Name': ['alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 25, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

# Display first few rows
print(df.head())

# Shape and info
print(df.shape)
print(df.info())

# Quick stats
print(df.describe())
