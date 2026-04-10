# Exoplanet searching tool

A Python tool that queries the NASA Exoplanet Archive for observable transiting hot Jupiter candidates and opens their ExoFOP follow-up observation pages directly in your browser.

## What it does

1. Queries the NASA Exoplanet Archive TAP service with science-driven filters
2. Returns a filtered list of hot Jupiter candidates observable from both hemispheres
3. Builds direct ExoFOP links for each planet
4. Opens ExoFOP pages in your browser for observation history lookup

## Filter Criteria

| Parameter | Value | Reason |
|---|---|---|
| Declination | -40° to +60° | Visible from both Hemispheres|
| Orbital period | 1–5 days | Hot Jupiter range, frequent transits |
| Transit depth | >0.5% | Detectable with 6-inch aperture |
| Stellar V magnitude | 8–11 | Bright enough without saturating sensor |
| Planet mass | >0.3 Jupiter masses | Confirmed gas giants only |

## Requirements

```
pip install requests pandas --break-system-packages
```

## Usage

```bash
python exofop_pipeline.py
```

The script will:
- Print the full filtered planet list in your terminal
- Save results to `planet_candidates.csv`
- Print all ExoFOP links
- Open the first 10 ExoFOP pages in your browser

To open all planets instead of just the first 10, edit this line in the script:

```python
for _, row in df.head(10).iterrows():   # change 10 to len(df) for all
```

## Output columns

| Column | Description |
|---|---|
| `pl_name` | Planet name |
| `ra` | Right Ascension (degrees) |
| `dec` | Declination (degrees) |
| `pl_orbper` | Orbital period (days) |
| `pl_trandep` | Transit depth (%) |
| `pl_bmassj` | Planet mass (Jupiter masses) |
| `sy_vmag` | Host star V-band magnitude |
| `exofop_url` | Direct link to ExoFOP target page |

Results are sorted by `sy_vmag` ascending — brightest stars first, which are the easiest targets for photometry.

## Why ExoFOP?

[ExoFOP](https://exofop.ipac.caltech.edu/tess/) is NASA's Exoplanet Follow-up Observing Program database. Each planet's page shows:
- Community-uploaded light curves (time series photometry)
- Number and recency of follow-up observations
- Spectroscopy and imaging data

Planets with few or no uploaded light curves are the most valuable targets for long-term amateur photometric monitoring.

## Data source

All planetary data is queried live from the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) `pscomppars` table via TAP (Table Access Protocol). Data is always up to date.

## Scientific context

This tool was built to support long-term transit timing variation (TTV) monitoring of hot Jupiters. Consistent ground-based photometric follow-up over years to decades can:

- Refine transit ephemerides (keeping timing predictions accurate)
- Detect orbital decay via period shortening
- Discover hidden outer planets through gravitational timing perturbations
- Constrain stellar tidal dissipation parameters

Even a null result after long-term monitoring is a significant scientific contribution — it constrains the dynamical architecture of the system to a measurable precision.

## License

MIT
