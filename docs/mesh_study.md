# Mesh Independence Study

Three mesh refinement levels were tested to assess grid convergence, plus a final C-domain mesh with improved topology.

## Mesh Configurations

### Mesh 1 — Coarse (Initial O-grid)

| Parameter | Value |
|---|---|
| Elements | 17,485 |
| Type | Structured O-grid quad |
| Domain | 51m × 30m rectangular |
| Purpose | Initial baseline |

### Mesh 2 — Medium (Triangular)

| Parameter | Value |
|---|---|
| Elements | 75,963 |
| Type | Unstructured triangular |
| Domain | 51m × 30m rectangular |
| Note | Abandoned after 0° and 4° due to triangular mesh limitations |

### Mesh 3 — Medium C-grid

| Parameter | Value |
|---|---|
| Elements | 48,000 |
| Type | C-grid with quadrilateral dominant |
| Domain | 51m × 30m rectangular outer |
| Inflation | 5e-5 first layer, 25 layers |
| Min orthogonal quality | 0.30 |

### Mesh 4 — Fine

| Parameter | Value |
|---|---|
| Elements | 118,529 |
| Type | C-grid with quadrilateral dominant |
| Domain | 51m × 30m rectangular outer |
| Inflation | 8.5e-6 first layer, 40 layers |
| Min orthogonal quality | 0.15 |

### Mesh 5 — C-Domain (Final)

| Parameter | Value |
|---|---|
| Elements | 108,890 |
| Type | Concentric C-domain with inflation |
| Domain | 70m × 40m C-shape |
| Inflation | 5e-5 first layer, 25 layers |
| Min orthogonal quality | 0.112 |
| Average orthogonal quality | 0.989 |

## Cl vs Mesh Refinement at 4° AoA

| Mesh | Elements | Cl | % of experimental (0.440) |
|---|---|---|---|
| Coarse | 17,485 | 0.128 | 29% |
| Medium C-grid | 48,000 | 0.197 | 45% |
| Fine | 118,529 | 0.185 | 42% |
| **C-Domain** | 108,890 | **0.294** | **67%** |

## Cl vs Mesh Refinement at 8° AoA

| Mesh | Elements | Cl | % of experimental (0.860) |
|---|---|---|---|
| Coarse | 17,485 | 0.280 | 33% |
| Medium C-grid | 48,000 | 0.412 | 48% |
| Fine | 118,529 | 0.389 | 45% |
| **C-Domain** | 108,890 | **0.581** | **68%** |

## Cl vs Mesh Refinement at 12° AoA

| Mesh | Elements | Cl | % of experimental (1.120) |
|---|---|---|---|
| Coarse | 17,485 | 0.566 | 51% |
| Medium C-grid | 48,000 | 0.915 | 82% |
| Fine | 118,529 | 0.880 | 79% |
| **C-Domain** | 108,890 | **0.850** | **76%** |

## Key Findings

1. **Element count alone is not sufficient** — the fine mesh (118k cells) gave worse Cl than the medium mesh (48k cells) due to topology issues
2. **Mesh topology matters more than refinement** — the C-domain mesh with 108k elements significantly outperformed the fine rectangular mesh
3. **Inflation layers achieved y⁺ < 1** on all C-grid meshes, confirming proper boundary layer resolution
4. **Quadrilateral dominant + Post inflation algorithm** is essential to avoid mesh control conflicts

## Mesh Quality Comparison

| Mesh | Avg Orthogonal | Min Orthogonal | Max Skewness |
|---|---|---|---|
| Coarse | ~0.92 | ~0.05 | >0.85 |
| Medium C-grid | 0.93 | 0.15 | <0.85 |
| Fine | 0.98 | 0.001 | >0.85 |
| **C-Domain** | **0.989** | **0.112** | **<0.50** |

The C-Domain mesh achieved the best quality metrics despite having fewer cells than the fine mesh.
