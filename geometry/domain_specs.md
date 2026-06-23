# Geometry Specifications

Complete coordinates and dimensions for reproducing the C-domain geometry in SpaceClaim or equivalent CAD software.

## Coordinate System

- Origin: (0, 0) at airfoil leading edge
- X-axis: chord direction (airfoil extends from X=0 to X=1)
- Y-axis: perpendicular to chord (positive up)
- Z-axis: 2D analysis (Z=0)

## Airfoil

| Parameter | Value |
|---|---|
| Profile | NACA 0012 |
| Chord length | 1 m |
| Leading edge | (0, 0) |
| Trailing edge | (1, 0) |
| Maximum thickness | 12% at 30% chord |

## Inner C-region (near-field, ~5 chord around airfoil)

### Semicircle (curved leading boundary)

| Parameter | Value |
|---|---|
| Center | (0, 0) |
| Radius | 5 m |
| Arc | Left half (from (0, 5) curving through (-5, 0) to (0, -5)) |

### Wake rectangle (continuing behind airfoil)

| Edge | Start | End |
|---|---|---|
| Top | (0, 5) | (15, 5) |
| Bottom | (0, -5) | (15, -5) |
| Right | (15, -5) | (15, 5) |

## Outer C-domain (far-field, ~20 chord around airfoil)

### Semicircle (curved leading boundary)

| Parameter | Value |
|---|---|
| Center | (0, 0) |
| Radius | 20 m |
| Arc | Left half (from (0, 20) curving through (-20, 0) to (0, -20)) |

### Wake rectangle (continuing behind airfoil)

| Edge | Start | End |
|---|---|---|
| Top | (0, 20) | (50, 20) |
| Bottom | (0, -20) | (50, -20) |
| Right | (50, -20) | (50, 20) |

## Surface Bodies

Two surface bodies created in SpaceClaim:

| Surface | Region | Description |
|---|---|---|
| Surface 1 | Inner C-region | Area between inner C-shape and airfoil |
| Surface 2 | Outer C-region | Area between outer C-shape and inner C-shape |

Both surfaces must be under one Component with Share Topology set to `Share` to ensure conformal mesh interface.

## Named Selections

| Edge | Named Selection | BC Type |
|---|---|---|
| Outer semicircle (left curve) | `inlet_velocity` | velocity-inlet |
| Outer wake top edge | `top` | pressure-outlet |
| Outer wake bottom edge | `bottom` | pressure-outlet |
| Outer wake right edge | `pressure_out` | pressure-outlet |
| Airfoil edges (upper + lower) | `airfoil` | wall |
| Inner C-boundary | (do not name) | interior |

## Domain Summary

| Parameter | Value |
|---|---|
| Total X extent | -20 to +50 m |
| Total Y extent | -20 to +20 m |
| Domain length | 70 m (70 chord lengths) |
| Domain height | 40 m (40 chord lengths) |
| Inner C radius | 5 m (5c) |
| Outer C radius | 20 m (20c) |
| Inner wake length | 14 m behind TE |
| Outer wake length | 49 m behind TE |
| Blockage ratio | 2.5% |
| Distance airfoil to upstream boundary | 20 m (20c) |
| Distance airfoil to downstream boundary | 49 m (49c) |

## SpaceClaim Construction Steps

1. **Create outer rectangle:** Sketch → Rectangle from (-20, -20) to (50, 20)
2. **Cut outer semicircle:** Sketch → Circle at (0,0), R=20m. Keep left half by drawing/cutting.
3. **Draw inner C-shape:** 
   - Sketch → Semicircle at (0,0), R=5m (left half)
   - Sketch → Rectangle from (0,-5) to (15,5)
4. **Import/draw NACA 0012** at (0,0) with chord 1m
5. **Create surfaces** using Fill or Planar tool:
   - Inner C-region surface
   - Outer C-region surface
6. **Apply Share Topology:** Select Component → Properties → Share Topology = `Share`
7. **Create Named Selections** for all boundaries
8. **Save** and update Workbench geometry cell
