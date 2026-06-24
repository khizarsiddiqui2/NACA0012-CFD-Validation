# C-Domain Mesh Results

Final C-domain mesh (108,890 cells) visualizations at all angles of attack.

## Mesh Visualizations

### Full Domain Overview
- **mesh_overview.png** — Complete C-domain showing concentric inner (R=5m) and outer (R=20m) C-shapes

### Airfoil Detail
- **mesh_airfoil_zoom.png** — NACA 0012 with 25-layer inflation layers
### Mesh Quality
- **mesh_Quality.png** — mesh quality

## Velocity Contours (0°, 4°, 8°, 12°)

- **velocity_0deg.png** — Symmetric flow, peak velocity ~44 m/s
- **velocity_4deg.png** — Upper surface acceleration to ~60.5 m/s, streamline deflection visible
- **velocity_8deg.png** — Strong acceleration to ~68 m/s, pronounced downwash
- **velocity_12deg.png** — Peak velocity ~72 m/s, near-stall behavior

## Pressure Contours (0°, 4°, 8°, 12°)

- **pressure_0deg.png** — Symmetric pressure distribution
- **pressure_4deg.png** — Suction peak on upper surface, stagnation point on lower surface
- **pressure_8deg.png** — Strong pressure asymmetry, increased suction peak
- **pressure_12deg.png** — Near-stall behavior, pressure recovery visible

## y+ Distribution

- **yplus_0deg.png** — Boundary layer resolution at 0°, y⁺ < 1.0
- **yplus_4deg.png** — Boundary layer resolution at 4°, y⁺ < 1.0
- **yplus_8deg.png** — Boundary layer resolution at 8°, y⁺ < 1.0
- **yplus_12deg.png** — Boundary layer resolution at 12°, y⁺ < 1.0

## Pathlines (Streamlines) (0°, 4°, 8°, 12°)

- **pathlines_0deg.png** — Symmetric streamlines, no net deflection
- **pathlines_4deg.png** — Clear upward deflection above airfoil, downwash in wake
- **pathlines_8deg.png** — Strong circulation, well-developed wake
- **pathlines_12deg.png** — Near-stall flow pattern, significant flow deflection

## Residual Convergence (0°, 4°, 8°, 12°)

- **residuals_0deg.png** — Machine precision convergence at 0°
- **residuals_4deg.png** — Convergence history at 4° (1st order + 2nd order phases)
- **residuals_8deg.png** — Convergence history at 8°
- **residuals_12deg.png** — Convergence history at 12° (near-stall oscillations)

## Results Summary

| α (°) | Cl_CFD | Cl_Exp | Accuracy | Cd_CFD | Cd_Exp |
|---|---|---|---|---|---|
| 0 | -0.00044 | 0.000 | ✓ symmetric | 0.00952 | 0.0080 |
| 4 | 0.294 | 0.440 | **67%** | 0.01621 | 0.0083 |
| 8 | 0.581 | 0.860 | **68%** | 0.03576 | 0.0116 |
| 12 | 0.850 | 1.120 | **76%** | 0.060 | 0.0190 |

**Average Cl Accuracy: 70%**

## Mesh & Solver Specifications

| Parameter | Value |
|---|---|
| Total Elements | 108,890 |
| Total Nodes | 109,162 |
| Orthogonal Quality (Avg) | 0.989 |
| Inflation Layers | 25 (growth 1.2) |
| y⁺ on Airfoil | < 1.0 |
| Turbulence Model | k-ω SST |
| Solver Scheme | Coupled |
| Discretization | 2nd Order Upwind |
| Domain Size | 70m × 40m |

EOF
cat /home/claude/NACA0012-CFD-Validation/images/cdomain/README.md
Output

# C-Domain Mesh Results

Final C-domain mesh (108,890 cells) visualizations at all angles of attack.

## Mesh Visualizations

### Full Domain Overview
- **mesh_overview.png** — Complete C-domain showing concentric inner (R=5m) and outer (R=20m) C-shapes

### Airfoil Detail
- **mesh_airfoil_zoom.png** — NACA 0012 with 25-layer inflation layers

## Velocity Contours (0°, 4°, 8°, 12°)

- **velocity_0deg.png** — Symmetric flow, peak velocity ~44 m/s
- **velocity_4deg.png** — Upper surface acceleration to ~60.5 m/s, streamline deflection visible
- **velocity_8deg.png** — Strong acceleration to ~68 m/s, pronounced downwash
- **velocity_12deg.png** — Peak velocity ~72 m/s, near-stall behavior

## Pressure Contours (0°, 4°, 8°, 12°)

- **pressure_0deg.png** — Symmetric pressure distribution
- **pressure_4deg.png** — Suction peak on upper surface, stagnation point on lower surface
- **pressure_8deg.png** — Strong pressure asymmetry, increased suction peak
- **pressure_12deg.png** — Near-stall behavior, pressure recovery visible


## Pathlines (Streamlines) (0°, 4°, 8°, 12°)

- **pathlines_0deg.png** — Symmetric streamlines, no net deflection
- **pathlines_4deg.png** — Clear upward deflection above airfoil, downwash in wake
- **pathlines_8deg.png** — Strong circulation, well-developed wake
- **pathlines_12deg.png** — Near-stall flow pattern, significant flow deflection

## Residual Convergence (0°, 4°, 8°, 12°)

- **residuals_0deg.png** — Machine precision convergence at 0°
- **residuals_4deg.png** — Convergence history at 4° (1st order + 2nd order phases)
- **residuals_8deg.png** — Convergence history at 8°
- **residuals_12deg.png** — Convergence history at 12° (near-stall oscillations)

## Results Summary

| α (°) | Cl_CFD | Cl_Exp | Accuracy | Cd_CFD | Cd_Exp |
|---|---|---|---|---|---|
| 0 | -0.00044 | 0.000 | ✓ symmetric | 0.00952 | 0.0080 |
| 4 | 0.294 | 0.440 | **67%** | 0.01621 | 0.0083 |
| 8 | 0.581 | 0.860 | **68%** | 0.03576 | 0.0116 |
| 12 | 0.850 | 1.120 | **76%** | 0.060 | 0.0190 |

**Average Cl Accuracy: 70%**

## Mesh & Solver Specifications

| Parameter | Value |
|---|---|
| Total Elements | 108,890 |
| Total Nodes | 109,162 |
| Orthogonal Quality (Avg) | 0.989 |
| Inflation Layers | 25 (growth 1.2) |
| y⁺ on Airfoil | < 1.0 |
| Turbulence Model | k-ω SST |
| Solver Scheme | Coupled |
| Discretization | 2nd Order Upwind |
| Domain Size | 70m × 40m |




