import pandas as pd

df = pd.read_excel("ABS Tech Case 2026_Data.xlsx")

df["HispanicLatino"] = df["HispanicLatino"].str.capitalize()


df.to_excel("Cleaned ABS Tech Case 2026_Data.xlsx", index=False)