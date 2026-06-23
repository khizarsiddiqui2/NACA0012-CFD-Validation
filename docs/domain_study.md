# Domain Topology Study

Three domain configurations were tested to identify the impact of outer boundary shape on lift prediction accuracy.

## Domain Configurations

### Domain 1 — Small Rectangular

| Parameter | Value |
|---|---|
| X extent | -13 to +37 m (50 m total) |
| Y extent | ±12.5 m (25 m total) |
| Blockage | ~4% |
| Outer shape | Rectangular |
| Inner C-grid | Yes |

### Domain 2 — Large Rectangular

| Parameter | Value |
|---|---|
| X extent | -30 to +50 m (80 m total) |
| Y extent | ±30 m (60 m total) |
| Blockage | ~1.7% |
| Outer shape | Rectangular |
| Inner C-grid | Yes |

### Domain 3 — C-Domain (Final)

| Parameter | Value |
|---|---|
| X extent | -20 to +50 m (70 m total) |
| Y extent | ±20 m (40 m total) |
| Blockage | 2.5% |
| Outer shape | C-shape (matches inner topology) |
| Inner C-grid | Yes |

## Cl Comparison at 4° AoA

| Domain | Cl | Cd | % accuracy |
|---|---|---|---|
| Small rectangular | 0.185 | 0.0165 | 42% |
| Large rectangular | 0.203 | 0.0167 | 46% |
| **C-Domain** | **0.294** | **0.0162** | **67%** |

## Cl Comparison at 8° AoA

| Domain | Cl | Cd | % accuracy |
|---|---|---|---|
| Small rectangular | 0.389 | 0.0376 | 45% |
| **C-Domain** | **0.581** | **0.0358** | **68%** |

## Key Insights

### Why rectangular outer domains underpredicted Cl

1. **Topology mismatch** — The rectangular outer domain forced flow to navigate around four corners, creating subtle flow disturbances that reduced circulation around the airfoil
2. **Pressure outlet behavior** — Rectangular outlets at sharp corners cannot properly handle angled exit flow at moderate AoA
3. **C-grid interface effects** — The transition between C-shaped inner mesh and rectangular outer mesh created localized flow distortion

### Why C-domain topology improved accuracy

1. **Smooth flow path** — Concentric C-shapes provide unobstructed flow development from inlet to outlet
2. **Conformal interfaces** — Matching topology means the interface between regions doesn't impose unphysical constraints
3. **Proper far-field BC behavior** — The curved velocity inlet allows undisturbed flow approach
4. **Lower wake exit constraints** — Rectangular wake exit at correct angle for flow direction

### Domain size vs topology

| Factor | Importance | Effect |
|---|---|---|
| Domain size | Moderate | 4° improvement from 50m → 80m rectangular |
| Domain shape | **Critical** | 21% improvement from rectangular → C-shape |

**Conclusion:** Domain topology matters significantly more than absolute size for airfoil CFD validation. A properly shaped C-domain outperforms a larger rectangular domain.
