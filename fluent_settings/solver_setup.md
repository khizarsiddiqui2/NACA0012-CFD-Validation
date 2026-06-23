# Ansys Fluent 2026 R1 — Complete Solver Setup

## 1. General Settings

| Field | Value |
|---|---|
| Solver Type | Pressure-Based |
| Velocity Formulation | Absolute |
| Time | Steady |
| 2D Space | Planar |

## 2. Models

| Model | Setting |
|---|---|
| Energy | Off |
| Viscous | k-omega SST |
| Multiphase | Off |
| Radiation | Off |

## 3. Materials

### Fluid: air (constant properties)

| Property | Value |
|---|---|
| Density | 1.225 kg/m³ |
| Viscosity | 1.7894 × 10⁻⁵ kg/(m·s) |
| Specific Heat | 1006.43 J/(kg·K) [not used, energy off] |

## 4. Cell Zone Conditions

| Zone | Type |
|---|---|
| component1-surface | fluid |

## 5. Boundary Conditions

### inlet_velocity (velocity-inlet)

| Field | Value |
|---|---|
| Velocity Specification Method | Magnitude and Direction |
| Reference Frame | Absolute |
| Velocity Magnitude | 43.8 m/s |
| X-Component | cos(α) — see table below |
| Y-Component | sin(α) — see table below |
| Supersonic/Initial Gauge Pressure | 0 Pa |
| Turbulence Specification | Intensity and Viscosity Ratio |
| Turbulent Intensity | 1 % |
| Turbulent Viscosity Ratio | 10 |

### Velocity components by angle of attack

| α | X-Component | Y-Component |
|---|---|---|
| 0° | 1.00000 | 0.00000 |
| 4° | 0.99756 | 0.06976 |
| 8° | 0.99027 | 0.13917 |
| 12° | 0.97815 | 0.20791 |

### pressure_out (pressure-outlet, rear)

| Field | Value |
|---|---|
| Backflow Reference Frame | Absolute |
| Gauge Pressure | 0 Pa |
| Backflow Direction Specification | Direction Vector |
| X-Component | matches inlet (cos α) |
| Y-Component | matches inlet (sin α) |
| Backflow Pressure Specification | Total Pressure |
| Prevent Reverse Flow | Unchecked |
| Backflow Turbulent Intensity | 1 % |
| Backflow Turbulent Viscosity Ratio | 10 |

### top (pressure-outlet)

| Field | Value |
|---|---|
| Gauge Pressure | 0 Pa |
| Prevent Reverse Flow | Checked |
| Backflow Turbulent Intensity | 1 % |
| Backflow Turbulent Viscosity Ratio | 10 |

### bottom (pressure-outlet)

| Field | Value |
|---|---|
| Gauge Pressure | 0 Pa |
| Prevent Reverse Flow | Checked |
| Backflow Turbulent Intensity | 1 % |
| Backflow Turbulent Viscosity Ratio | 10 |

### airfoil (wall)

| Field | Value |
|---|---|
| Wall Motion | Stationary Wall |
| Shear Condition | No Slip |

## 6. Reference Values

Compute From: inlet_velocity

| Field | Value |
|---|---|
| Area | 1 m² |
| Density | 1.225 kg/m³ |
| Depth | 1 m |
| Length | 1 m |
| Pressure | 0 Pa |
| Temperature | 288.16 K |
| Velocity | 43.8 m/s |
| Viscosity | 1.7894 × 10⁻⁵ kg/(m·s) |
| Ratio of Specific Heats | 1.4 |

## 7. Solution Methods

| Field | Value |
|---|---|
| Pressure-Velocity Coupling Scheme | **Coupled** |
| Flux Type | Rhie-Chow: momentum based (Auto Select) |
| Gradient | Least Squares Cell Based |
| Pressure | Second Order |
| Momentum | Second Order Upwind |
| Turbulent Kinetic Energy | Second Order Upwind |
| Specific Dissipation Rate | Second Order Upwind |
| Pseudo Time Method | Off |
| Warped-Face Gradient Correction | Off |
| High Order Term Relaxation | Off |

## 8. Solution Controls

### First Order Phase (initial 200-500 iterations)

| Parameter | Value |
|---|---|
| Flow Courant Number | 100 |
| Explicit Momentum | 0.75 |
| Explicit Pressure | 0.75 |
| Density | 1 |
| Body Forces | 1 |
| Turbulent Kinetic Energy | 0.8 |
| Specific Dissipation Rate | 0.8 |
| Turbulent Viscosity | 0.95 |

### Second Order Phase (after first-order convergence)

| Parameter | Value |
|---|---|
| Flow Courant Number | 50 |
| Explicit Momentum | 0.5 |
| Explicit Pressure | 0.5 |
| Density | 1 |
| Body Forces | 1 |
| Turbulent Kinetic Energy | 0.7 |
| Specific Dissipation Rate | 0.7 |
| Turbulent Viscosity | 0.9 |

## 9. Solution Initialization

| Field | Value |
|---|---|
| Initialization Method | Standard Initialization |
| Compute From | inlet_velocity |

## 10. Residual Monitors

| Equation | Absolute Criteria | Check Convergence |
|---|---|---|
| continuity | 1e-6 | Off (monitor visually) |
| x-velocity | 1e-9 | Off |
| y-velocity | 1e-9 | Off |
| k | 1e-6 | Off |
| omega | 1e-6 | Off |

Iterations to Plot: 2000
Iterations to Store: 2000

## 11. Force Reports

Results → Reports → Forces

### Lift Direction Vectors

| α | X | Y |
|---|---|---|
| 0° | 0.00000 | 1.00000 |
| 4° | -0.06976 | 0.99756 |
| 8° | -0.13917 | 0.99027 |
| 12° | -0.20791 | 0.97815 |

### Drag Direction Vectors

| α | X | Y |
|---|---|---|
| 0° | 1.00000 | 0.00000 |
| 4° | 0.99756 | 0.06976 |
| 8° | 0.99027 | 0.13917 |
| 12° | 0.97815 | 0.20791 |

Wall Zone: airfoil

## 12. Run Calculation

### Phase 1 (First Order)

- Iterations: 500
- Click Calculate
- Verify residuals dropping smoothly
- Check Cl/Cd stabilizing

### Phase 2 (Second Order)

After Phase 1 converges:
- Change Methods (Momentum, TKE, Spec Diss) to Second Order Upwind
- Reduce Flow Courant to 50
- Reduce explicit relaxations to 0.5
- **Do not reinitialize**
- Run additional 1500-3000 iterations to deep convergence

### Convergence Criteria

Solution is converged when:
- All velocity residuals below 1e-8
- Continuity residual below 1e-4
- Cl plot completely flat for last 500 iterations
- Cd plot completely flat for last 500 iterations

## 13. Save Case File

After convergence:
- File → Write → Case & Data
- Filename format: `NACA0012_Cdomain_[angle]deg.cas.h5`
