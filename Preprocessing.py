import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_excel("ABS Tech Case 2026_Data.xlsx")

# Columns to scale
cols_to_scale = [
    "EngagementSurvey", "EmpSatisfaction", "SpecialProjectsCount",
    "DaysLateLast30", "Absences", "ManPos", "TechLev", "JobStr",
    "ProjColl", "ProjSelf", "ProjLead", "TeamIden", "OrgIden",
    "CarOpp", "PsySafe", "Feedback", "Trust", "Network",
    "AIUse", "AIConf", "TrainHours", "WLF", "InnoCont"
]

# Convert selected columns to numeric (in case Excel stored them as text)
df[cols_to_scale] = df[cols_to_scale].apply(pd.to_numeric, errors="coerce")

# Standardize only the selected columns
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[cols_to_scale])

# Put scaled values back into the original dataframe
df[cols_to_scale] = df_scaled

# Save full dataset with scaled columns
df.to_excel("Cleaned_ABS_Tech_Case_2026_Data.xlsx", index=False)