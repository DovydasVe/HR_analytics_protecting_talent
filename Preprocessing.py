import pandas as pd
from sklearn.preprocessing import StandardScalegr

df = pd.read_excel("ABS Tech Case 2026_Data.xlsx")

# Capitalize the first letter of each word in the "HispanicLatino" column
df["HispanicLatino"] = df["HispanicLatino"].str.capitalize()

# Encode categorical variables (convert to dummy variables)
df_encoded = pd.get_dummies(df, drop_first=True)

# Initialize scaler
scaler = StandardScaler()

# Standardize all columns
df_standardized = pd.DataFrame(
    scaler.fit_transform(df_encoded),
    columns=df_encoded.columns,
    index=df_encoded.index
)

df.to_excel("Cleaned ABS Tech Case 2026_Data.xlsx", index=False)