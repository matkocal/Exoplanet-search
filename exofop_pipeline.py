import requests
import pandas as pd
from io import StringIO
import webbrowser
import time

# --- QUERY --- edit this to change your filters ---
query = """
SELECT pl_name, ra, dec, pl_orbper, pl_trandep, pl_bmassj, sy_vmag
FROM pscomppars
WHERE dec BETWEEN -40 AND 60
AND pl_orbper BETWEEN 1 AND 5
AND pl_trandep > 0.5
AND sy_vmag BETWEEN 8 AND 11
AND pl_bmassj > 0.3
ORDER BY sy_vmag ASC
"""

# --- do not edit below this line ---

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
response = requests.get(url, params={"query": query, "format": "csv"})
df = pd.read_csv(StringIO(response.text))

print(f"Found {len(df)} planets\n")
print(df.to_string(index=False))

df["hostname"] = df["pl_name"].str.replace(r"\s+[a-z]$", "", regex=True)
df["exofop_url"] = "https://exofop.ipac.caltech.edu/tess/target.php?id=" + df["hostname"]
df.to_csv("planet_candidates.csv", index=False)
print(f"\nSaved to planet_candidates.csv")

print("\n--- ExoFOP Links ---")
for _, row in df.iterrows():
    print(f"{row['pl_name']:30s}  ->  {row['exofop_url']}")

print(f"\nOpening first 10 in browser...")
for _, row in df.head(10).iterrows():
    webbrowser.open(row["exofop_url"])
    time.sleep(0.5)
