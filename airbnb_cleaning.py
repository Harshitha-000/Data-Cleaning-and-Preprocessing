import pandas as pd

df = pd.read_excel("AB_NYC_2019.xlsx")

print(df.head())
print("File loaded successfully!")

print(df.isnull().sum())


df['name'] = df['name'].fillna("Unknown")
df['host_name'] = df['host_name'].fillna("Unknown")
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

df['last_review'] = pd.to_datetime(df['last_review'])

print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

df['neighbourhood_group'] = df['neighbourhood_group'].str.lower()
df['room_type'] = df['room_type'].str.lower()

df = df[(df['price'] > 0) & (df['price'] < 1000)]
df = df[df['minimum_nights'] < 365]

print(df.info())
print(df.describe())
print(df.isnull().sum())

df.to_csv("AB_NYC_2019_cleaned.csv", index=False)
print("Cleaned file saved successfully!")
