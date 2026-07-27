# 1. Type-safe Input Parser
import pandas as pd
raw = {'age':['20'], "score": ["98.5"], "active": ["Yes"]}
df = pd.DataFrame(raw)
df['age'] = pd.to_numeric(df["age"], errors='coerce').fillna(0).astype(int)
df['score'] = pd.to_numeric(df["score"], errors='coerce').fillna(0.0)
df['active'] = df['active'].str.lower().isin(['yes','true',"1"])
print(df.to_dict(orient='records')[0])