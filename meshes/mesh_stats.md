# Mesh Statistics Summary

## Final C-Domain Mesh (Production Mesh)

| Metric | Value |
|---|---|
| Total Elements | 108,890 |
| Total Nodes | 109,162 |
| Element Types | Quad-dominant + Tri (mostly Quad4) |
| Bounding Box Diagonal | 80.6 m |
| Minimum Edge Length | 2.52 × 10⁻³ m |

### Quality Metrics

| Metric | Min | Max | Average | Std Dev |
|---|---|---|---|---|
| Orthogonal Quality | 0.112 | 1.000 | 0.989 | 0.039 |
| Skewness | 0 | ~0.5 | ~0.05 | low |
| Aspect Ratio | 1 | <700 | low | — |

### Boundary Layer Resolution

| Parameter | Value |
|---|---|
| First Layer Height | 5 × 10⁻⁵ m |
| Maximum Layers | 25 |
| Growth Rate | 1.2 |
| Inflation Algorithm | Post |
| y⁺ on airfoil | < 1 (target met) |

## Mesh Controls Applied

1. **Quadrilateral Dominant Method** on inner C-region
2. **Edge Sizing** on airfoil — 300 divisions, Hard behavior
3. **Inflation** on airfoil — 25 layers, 5e-5 first layer, growth 1.2, Post algorithm
4. **Body Sizing** on inner C-region — 0.05 m element size, Soft
5. **Body Sizing** on outer C-region — 0.5 m element size, Soft
6. **Edge Sizing** on wake rectangle (3 edges) — 80 divisions, No Bias

## Element Distribution

- Inner C-region: ~75% of elements (high resolution near airfoil)
- Outer C-region: ~25% of elements (coarse far-field)
- Inflation layers: ~12,000 cells in 25 layers around airfoil

## Comparison Across All Meshes Tested

| Mesh | Elements | Avg OQ | Min OQ | Domain | Cl @ 4° |
|---|---|---|---|---|---|
| Coarse O-grid | 17,485 | ~0.92 | ~0.05 | 51×30 rect | 0.128 |
| Medium triangular | 75,963 | — | — | 51×30 rect | 0.136 |
| Medium C-grid | 48,000 | 0.93 | 0.15 | 51×30 rect | 0.197 |
| Fine | 118,529 | 0.98 | 0.001 | 51×30 rect | 0.185 |
| Large rect | 115,893 | 0.99 | 0.30 | 80×60 rect | 0.203 |
| **C-Domain** | **108,890** | **0.989** | **0.112** | **70×40 C** | **0.294** |

The C-Domain mesh achieves the best quality metrics and the highest Cl accuracy.
