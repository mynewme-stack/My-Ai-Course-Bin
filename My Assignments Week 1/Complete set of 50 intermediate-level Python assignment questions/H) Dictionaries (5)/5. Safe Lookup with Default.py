# Safe Lookup with Default
import pandas as pd
s = pd.Series({'name':'Abdul','age':20})
missing = []
val = s.get('email', missing.append(1) or 'N/A')
print(val)
print(len(missing))