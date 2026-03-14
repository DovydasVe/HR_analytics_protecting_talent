import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("ABS Tech Case 2026_Data.xlsx")
df["HispanicLatino"] = df["HispanicLatino"].str.capitalize()

cols_to_scale = [
    "EngagementSurvey", "EmpSatisfaction", "SpecialProjectsCount",
    "DaysLateLast30", "Absences", "ManPos", "TechLev", "JobStr",
    "ProjColl", "ProjSelf", "ProjLead", "TeamIden", "OrgIden",
    "CarOpp", "PsySafe", "Feedback", "Trust", "Network",
    "AIUse", "AIConf", "TrainHours", "WLF", "InnoCont",
    "PerfScore"
]

df[cols_to_scale] = df[cols_to_scale].apply(pd.to_numeric, errors="coerce")

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[cols_to_scale])

df[cols_to_scale] = df_scaled

df.to_excel("Cleaned_ABS_Tech_Case_2026_Data.xlsx", index=False)