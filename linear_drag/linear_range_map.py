#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ============================================================
# Projectile Motion in Python
# Linear-drag model: horizontal range R(theta, gamma)
# ============================================================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import brentq


# Plot style
mpl.rcParams["text.usetex"] = False
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.rcParams["mathtext.fontset"] = "stix"


# Physical parameters (SI units)
g = 9.81       # m/s^2
v0 = 20.0      # m/s


# Parameter grids
theta_deg = np.linspace(15.0, 75.0, 500)   # degrees
gamma_values = np.linspace(0.0, 1.0, 300)  # 1/s

theta_rad = np.deg2rad(theta_deg)


# Ideal horizontal range
def ideal_range(theta):

    return (v0**2/g)*np.sin(2.0*theta)


# Linear-drag horizontal range
def linear_range(theta, gamma):

    # Ideal limit: gamma = 0
    if gamma == 0.0:

        return ideal_range(theta)

    # Exact vertical position
    def y_exact(t):

        return (
            (v0*np.sin(theta) + g/gamma)
            * (1.0 - np.exp(-gamma*t))/gamma
            - (g/gamma)*t
        )

    # Ideal flight time used only to bracket
    # the nonzero root of y(T) = 0
    T_ideal = 2.0*v0*np.sin(theta)/g

    # Exact flight time
    T = brentq(
        y_exact,
        1.0e-8,
        2.0*T_ideal + 2.0,
    )

    # Exact horizontal range
    R = (
        v0*np.cos(theta)/gamma
        * (1.0 - np.exp(-gamma*T))
    )

    return R


# ------------------------------------------------------------
# Horizontal-range map R(theta, gamma)
# ------------------------------------------------------------

R = np.zeros(
    (len(gamma_values), len(theta_deg))
)

theta_opt = np.zeros(
    len(gamma_values)
)


for i, gamma in enumerate(gamma_values):

    for j, theta in enumerate(theta_rad):

        R[i, j] = linear_range(
            theta,
            gamma,
        )

    # Angle corresponding to the maximum range
    index_max = np.argmax(R[i, :])

    theta_opt[i] = theta_deg[index_max]


# -------- Plot --------

plt.figure(figsize=(6.8, 4.5))


# Filled contour
# Color represents the horizontal range
cs = plt.contourf(
    theta_deg,
    gamma_values,
    R,
    levels=30,
    cmap="cividis",
)


# Color bar
cbar = plt.colorbar(cs)

cbar.set_label(
    r"$R\ \mathrm{[m]}$",
    fontsize=13,
)

cbar.ax.tick_params(
    labelsize=11,
)


# Iso-range contours
# No numerical labels are displayed
plt.contour(
    theta_deg,
    gamma_values,
    R,
    levels=10,
    colors="k",
    linewidths=0.6,
    alpha=0.55,
)


# Optimal-angle curve
plt.plot(
    theta_opt,
    gamma_values,
    linestyle="--",
    linewidth=2,
    color="white",
    label=r"$\theta_{\mathrm{opt}}(\gamma)$",
)


# Axes and ticks
plt.xlabel(
    r"$\theta\ \mathrm{[deg]}$",
    fontsize=14,
)

plt.ylabel(
    r"$\gamma\ \mathrm{[s^{-1}]}$",
    fontsize=14,
)

plt.xticks(
    np.arange(15, 76, 15),
    fontsize=12,
)

plt.yticks(
    np.arange(0.0, 1.01, 0.2),
    fontsize=12,
)

plt.xlim(15.0, 75.0)
plt.ylim(0.0, 1.0)


# Legend
plt.legend(
    loc="upper right",
    fontsize=11,
    frameon=True,
)


plt.grid(False)
plt.tight_layout()


# Save figure
plt.savefig(
    "linear_range_map.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "linear_range_map.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:




