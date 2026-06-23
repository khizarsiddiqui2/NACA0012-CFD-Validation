"""
NACA 0012 CFD Validation - Plotting Script
Generates comparison plots of Cl and Cd vs angle of attack for all meshes
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
coeffs = pd.read_csv('coefficients.csv')
exp = pd.read_csv('experimental_data.csv')

# Plot Cl vs alpha
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(coeffs['alpha_deg'], coeffs['Cl_coarse'], 'o--', label='Coarse (17k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cl_medium'], 's--', label='Medium (48k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cl_fine'], '^--', label='Fine (118k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cl_Cdomain'], 'D-', label='C-Domain (108k cells)', 
        linewidth=2, color='red', markersize=8)
ax.plot(exp['alpha_deg'], exp['Cl_exp'], 'k-', label='Experimental (Ladson)', linewidth=2)

ax.set_xlabel('Angle of Attack α (°)', fontsize=12)
ax.set_ylabel('Lift Coefficient Cl', fontsize=12)
ax.set_title('NACA 0012 — Lift Coefficient vs Angle of Attack\nRe = 3×10⁶, k-ω SST', fontsize=13)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.1, 1.4)

plt.tight_layout()
plt.savefig('Cl_vs_alpha.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot Cd vs alpha
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(coeffs['alpha_deg'], coeffs['Cd_coarse'], 'o--', label='Coarse (17k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cd_medium'], 's--', label='Medium (48k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cd_fine'], '^--', label='Fine (118k cells)', alpha=0.6)
ax.plot(coeffs['alpha_deg'], coeffs['Cd_Cdomain'], 'D-', label='C-Domain (108k cells)', 
        linewidth=2, color='red', markersize=8)
ax.plot(exp['alpha_deg'], exp['Cd_exp'], 'k-', label='Experimental (Ladson)', linewidth=2)

ax.set_xlabel('Angle of Attack α (°)', fontsize=12)
ax.set_ylabel('Drag Coefficient Cd', fontsize=12)
ax.set_title('NACA 0012 — Drag Coefficient vs Angle of Attack\nRe = 3×10⁶, k-ω SST', fontsize=13)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(-1, 17)

plt.tight_layout()
plt.savefig('Cd_vs_alpha.png', dpi=300, bbox_inches='tight')
plt.show()

# Lift-to-Drag ratio
fig, ax = plt.subplots(figsize=(10, 6))

# Only plot where Cd is non-zero (skip 0 degree)
mask = coeffs['alpha_deg'] > 0
ax.plot(coeffs.loc[mask, 'alpha_deg'], 
        coeffs.loc[mask, 'Cl_Cdomain']/coeffs.loc[mask, 'Cd_Cdomain'], 
        'D-', label='C-Domain CFD', linewidth=2, color='red', markersize=8)

mask_exp = exp['alpha_deg'] > 0
ax.plot(exp.loc[mask_exp, 'alpha_deg'], 
        exp.loc[mask_exp, 'Cl_exp']/exp.loc[mask_exp, 'Cd_exp'], 
        'k-', label='Experimental (Ladson)', linewidth=2)

ax.set_xlabel('Angle of Attack α (°)', fontsize=12)
ax.set_ylabel('Lift-to-Drag Ratio L/D', fontsize=12)
ax.set_title('NACA 0012 — Lift-to-Drag Ratio\nRe = 3×10⁶', fontsize=13)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('LtoD_vs_alpha.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plots generated successfully!")
print(f"\nSummary at 4 degrees:")
print(f"  CFD Cl: {coeffs[coeffs['alpha_deg']==4]['Cl_Cdomain'].values[0]:.4f}")
print(f"  Exp Cl: {exp[exp['alpha_deg']==4]['Cl_exp'].values[0]:.4f}")
print(f"  Accuracy: {coeffs[coeffs['alpha_deg']==4]['Cl_Cdomain'].values[0]/exp[exp['alpha_deg']==4]['Cl_exp'].values[0]*100:.1f}%")
