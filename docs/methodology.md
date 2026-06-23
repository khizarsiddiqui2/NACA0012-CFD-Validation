# CFD Methodology

## Geometry

The computational domain uses a concentric C-domain topology with matching inner and outer C-shapes. This design eliminates the artificial blockage caused by mismatched rectangular outer domains with C-grid inner regions.

### Inner C-region (near-field)

| Element | Coordinates / Dimension |
|---|---|
| Semicircle center | (0, 0) |
| Semicircle radius | 5 m |
| Wake rectangle top | (0, 5) to (15, 5) |
| Wake rectangle bottom | (0, -5) to (15, -5) |
| Wake rectangle right | (15, -5) to (15, 5) |

### Outer C-domain (far-field)

| Element | Coordinates / Dimension |
|---|---|
| Semicircle center | (0, 0) |
| Semicircle radius | 20 m |
| Wake rectangle top | (0, 20) to (50, 20) |
| Wake rectangle bottom | (0, -20) to (50, -20) |
| Wake rectangle right | (50, -20) to (50, 20) |

### Airfoil

| Parameter | Value |
|---|---|
| Profile | NACA 0012 |
| Chord | 1 m |
| Leading edge | (0, 0) |
| Trailing edge | (1, 0) |

### Domain summary

| Parameter | Value |
|---|---|
| X extent | -20 to +50 m (70 chord) |
| Y extent | -20 to +20 m (40 chord) |
| Blockage ratio | 2.5% |

## Meshing Strategy

### Global settings

| Field | Value |
|---|---|
| Physics Preference | CFD |
| Solver Preference | Fluent |
| Element Size | 0.5 m |
| Growth Rate | 1.15 |
| Mesh Defeaturing | No |
| Capture Curvature | Yes (1e-4 m min) |
| Capture Proximity | Yes (1e-4 m min) |

### Mesh controls (applied in order)

**1. Quadrilateral Dominant Method** on inner C-region

**2. Edge Sizing on airfoil**
- Named Selection: `airfoil`
- Number of Divisions: 300
- Behavior: Hard

**3. Inflation on airfoil**
- Scoping: inner C-region face
- Boundary: airfoil edges
- First Layer Thickness: 5 × 10⁻⁵ m
- Maximum Layers: 25
- Growth Rate: 1.2
- Algorithm: Post

**4. Body Sizing on inner C-region**
- Element Size: 0.05 m
- Behavior: Soft

**5. Body Sizing on outer C-region**
- Element Size: 0.5 m
- Behavior: Soft

**6. Edge Sizing on wake rectangle (3 edges)**
- Number of Divisions: 80
- Bias: No Bias

### Critical mesh insights

- **Inflation Algorithm must be Post** to avoid conflicts with Quadrilateral Dominant method
- **Avoid aggressive bias factors** (>3) on wake edges — creates high-aspect-ratio cells that destabilize the solver
- **Share Topology** must be set to `Share` in SpaceClaim Component properties to ensure conformal interface between inner and outer regions
- **Defeature Size** must be very small (1e-6 m) or disabled to prevent geometry simplification removing airfoil features

### Final mesh statistics

| Metric | Value |
|---|---|
| Total elements | 108,890 |
| Total nodes | 109,162 |
| Min orthogonal quality | 0.112 |
| Average orthogonal quality | 0.989 |
| Standard deviation | 0.039 |
| Max aspect ratio | < 700 |
| y⁺ on airfoil | < 1 |

## Boundary Conditions

| Boundary | Type | Settings |
|---|---|---|
| inlet_velocity | velocity-inlet | Magnitude + Direction, TI=1%, TVR=10 |
| pressure_out | pressure-outlet | 0 Pa, Direction Vector method |
| top | pressure-outlet | 0 Pa, Prevent Reverse Flow |
| bottom | pressure-outlet | 0 Pa, Prevent Reverse Flow |
| airfoil | wall | No-slip, stationary |

### Velocity components per angle of attack

| α | Vx (cos α) | Vy (sin α) |
|---|---|---|
| 0° | 1.00000 | 0.00000 |
| 4° | 0.99756 | 0.06976 |
| 8° | 0.99027 | 0.13917 |
| 12° | 0.97815 | 0.20791 |

## Solver Setup

### Models

- Solver: Pressure-Based
- Velocity Formulation: Absolute
- Time: Steady
- 2D Space: Planar
- Energy: Off
- Viscous: k-ω SST

### Methods

| Field | Value |
|---|---|
| Pressure-Velocity Coupling | **Coupled** |
| Gradient | Least Squares Cell Based |
| Pressure | Second Order |
| Momentum | Second Order Upwind |
| Turbulent KE | Second Order Upwind |
| Specific Dissipation Rate | Second Order Upwind |
| Pseudo Time Method | Off |

### Solution Controls

| Parameter | First Order Phase | Second Order Phase |
|---|---|---|
| Flow Courant Number | 100 | 50 |
| Explicit Momentum | 0.75 | 0.5 |
| Explicit Pressure | 0.75 | 0.5 |
| Turbulent KE | 0.8 | 0.7 |
| Specific Dissipation | 0.8 | 0.7 |
| Turbulent Viscosity | 0.95 | 0.9 |

### Reference Values

Computed from inlet_velocity:
- Area: 1 m²
- Density: 1.225 kg/m³
- Velocity: 43.8 m/s
- Length: 1 m

## Convergence Strategy

The Coupled solver with under-relaxation phasing achieves machine-precision convergence:

1. **Standard Initialization** from inlet_velocity
2. **First Order Phase** — 500 iterations to develop stable flow field
3. **Switch to Second Order** with reduced Courant number
4. **Continue iterating** to deep convergence (1500-3000 additional iterations)
5. **Verify** Cl/Cd plots fully flat over last 500 iterations

### Why Coupled instead of SIMPLE

Initial attempts with SIMPLE scheme failed to converge with the C-domain mesh due to:
- High cell volume ratio between inflation layer and far-field cells
- Complex flow physics at high angles of attack

The Coupled solver handles these conditions robustly and converges in significantly fewer iterations.

## Force Coefficient Calculation

Lift and drag direction vectors per angle of attack:

| α | Lift Vector (X, Y) | Drag Vector (X, Y) |
|---|---|---|
| 0° | (0, 1) | (1, 0) |
| 4° | (-0.06976, 0.99756) | (0.99756, 0.06976) |
| 8° | (-0.13917, 0.99027) | (0.99027, 0.13917) |
| 12° | (-0.20791, 0.97815) | (0.97815, 0.20791) |

Forces reported on `airfoil` wall zone using:
- Results → Reports → Forces
