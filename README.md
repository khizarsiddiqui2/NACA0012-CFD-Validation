# NACA 0012 CFD Validation Study

2D RANS validation study of the NACA 0012 airfoil at Re = 3 × 10⁶ using Ansys Fluent 2026 R1, compared against Ladson et al. experimental data (NASA TM-4074).

## Project Overview

This study validates a 2D steady-state CFD methodology for low-speed airfoil aerodynamics. Four mesh configurations and two domain topologies were tested to identify the impact of mesh quality and domain shape on lift and drag prediction accuracy.

**Key finding:** Matching the outer domain topology to the inner C-grid (concentric C-shapes) improved Cl prediction accuracy from 45% to 70% of experimental values at moderate angles of attack.

## Flow Conditions

| Parameter | Value |
|---|---|
| Reynolds number | 3 × 10⁶ |
| Mach number | 0.15 |
| Free-stream velocity | 43.8 m/s |
| Chord length | 1.0 m |
| Density | 1.225 kg/m³ |
| Dynamic viscosity | 1.7894 × 10⁻⁵ kg/(m·s) |
| Turbulence model | k-ω SST |
| Inlet turbulence intensity | 1% |
| Inlet turbulent viscosity ratio | 10 |

## Final Results (C-Domain Mesh)

| α (°) | Cl_CFD | Cl_exp | Cl accuracy | Cd_CFD | Cd_exp |
|---|---|---|---|---|---|
| 0 | -0.00044 | 0.000 | ✓ | 0.00952 | 0.0080 |
| 4 | 0.294 | 0.440 | 67% | 0.01621 | 0.0083 |
| 8 | 0.581 | 0.860 | 68% | 0.03576 | 0.0116 |
| 12 | 0.850 | 1.120 | 76% | 0.060 | 0.0190 |

Average Cl accuracy: **70%**

## Methodology Summary

- **Geometry:** Concentric C-domain topology built in SpaceClaim
- **Meshing:** Quadrilateral-dominant with 25-layer inflation (y⁺ < 1)
- **Solver:** Coupled pressure-velocity, Second Order Upwind
- **Convergence:** Machine precision residuals (1e-9 to 1e-12 on velocities)

Detailed methodology available in [docs/methodology.md](docs/methodology.md).

## Repository Structure

```
NACA0012-CFD-Validation/
├── README.md                    Project overview
├── docs/                        Detailed documentation
│   ├── methodology.md           Full CFD methodology
│   ├── mesh_study.md            Grid independence analysis
│   └── domain_study.md          Domain topology comparison
├── geometry/                    Geometry specifications
│   └── domain_specs.md          Dimensions and topology
├── meshes/                      Mesh data and statistics
│   └── mesh_stats.md            Quality metrics for all meshes
├── results/                     Numerical results
│   ├── coefficients.csv         All Cl/Cd values
│   └── experimental_data.csv    Ladson reference data
├── fluent_settings/             Solver configuration
│   └── solver_setup.md          Complete Fluent settings
├── validation/                  Comparison analysis
│   └── comparison_analysis.md   CFD vs experimental
└── images/                      Plots and contours 

## How to Reproduce

1. Build geometry in SpaceClaim using [geometry/domain_specs.md](geometry/domain_specs.md)
2. Mesh in Ansys Meshing using settings in [docs/methodology.md](docs/methodology.md)
3. Set up Fluent using [fluent_settings/solver_setup.md](fluent_settings/solver_setup.md)
4. Run all four angles of attack (0°, 4°, 8°, 12°)
5. Compare results against [results/experimental_data.csv](results/experimental_data.csv)

## Author

Khizar Siddiqui
Aerospace/Mechanical Engineer
Saudi Council of Engineers (SCE) Registered

## Reference

Ladson, C.L. (1988). "Effects of Independent Variation of Mach and Reynolds Numbers on the Low-Speed Aerodynamic Characteristics of the NACA 0012 Airfoil Section." NASA TM-4074.

## License

MIT License — see LICENSE file
