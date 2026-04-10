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
