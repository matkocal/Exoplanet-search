import requests
import pandas as pd
from io import StringIO
import webbrowser
import time

# --- 1. Query NASA Exoplanet Archive ---
query = """
SELECT pl_name, ra, dec, pl_orbper, pl_trandep, pl_bmassj, sy_vmag
FROM pscomppars
WHERE dec BETWEEN -40 AND 60
AND pl_orbper BETWEEN 1 AND 5
AND pl_trandep > 0.005
AND sy_vmag BETWEEN 8 AND 11
AND pl_bmassj > 0.3
AND pl_name LIKE 'WASP%'
ORDER BY sy_vmag ASC
"""

print("Fetching WASP planets from NASA Archive...")
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
response = requests.get(url, params={"query": query, "format": "csv"})
df = pd.read_csv(StringIO(response.text))
print(f"Found {len(df)} WASP planets matching your filters\n")
print(df.to_string(index=False))

# --- 2. Build ExoFOP URLs ---
# ExoFOP searches by hostname (star name), not planet name
# WASP-43 b -> hostname is WASP-43
df["hostname"] = df["pl_name"].str.extract(r"^(WASP-\d+)")
df["exofop_url"] = "https://exofop.ipac.caltech.edu/tess/target.php?id=" + df["hostname"]

print("\n--- ExoFOP Links ---")
for _, row in df.iterrows():
    print(f"{row['pl_name']:20s}  ->  {row['exofop_url']}")

# --- 3. Open all in browser (comment out if too many tabs) ---
print("\nOpening ExoFOP pages in browser...")
for _, row in df.iterrows():
    webbrowser.open(row["exofop_url"])
    time.sleep(0.5)  # small delay so browser doesn't get overwhelmed
