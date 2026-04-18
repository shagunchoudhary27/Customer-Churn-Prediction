import pandas as pd

df = pd.read_csv("data.csv")

print("Missing Values:")
print(df.isnull().sum())

print("Dataset Shape:", df.shape)