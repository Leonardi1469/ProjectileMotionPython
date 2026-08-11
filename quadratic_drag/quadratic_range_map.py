#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ============================================================
# Projectile Motion in Python
# Quadratic-drag model: horizontal range R(theta, kappa)
# ============================================================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Plot style
mpl.rcParams["text.usetex"] = False
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.rcParams["mathtext.fontset"] = "stix"


# Physical parameters (SI units)
g = 9.81       # m/s^2
v0 = 20.0      # m/s


# Parameter grids
theta_deg = np.linspace(15.0, 75.0, 500)    # degrees
kappa_values = np.linspace(0.0, 0.20, 300)  # 1/m

theta_rad = np.deg2rad(theta_deg)


# Ideal horizontal range
def ideal_range(theta):

    return (v0**2/g)*np.sin(2.0*theta)


# Quadratic-drag model
# State vector: [x, y, vx, vy]
def quadratic_model(t, state, kappa):

    x, y, vx, vy = state

    # Instantaneous speed
    speed = np.hypot(vx, vy)

    return [
        vx,
        vy,
        -kappa*speed*vx,
        -g-kappa*speed*vy,
    ]


# Ground-impact event
# The integration stops when the projectile returns to y = 0.
def ground_event(t, state, kappa):

    if t < 1.0e-8:
        return 1.0

    return state[1]


ground_event.terminal = True
ground_event.direction = -1


# Horizontal range
def quadratic_range(theta, kappa):

    # Ideal limit: kappa = 0
    if kappa == 0.0:

        return ideal_range(theta)

    # Initial conditions
    state0 = [
        0.0,
        0.0,
        v0*np.cos(theta),
        v0*np.sin(theta),
    ]

    solution = solve_ivp(
        quadratic_model,
        (0.0, 20.0),
        state0,
        args=(kappa,),
        events=ground_event,
        max_step=0.02,
        rtol=1e-9,
        atol=1e-11,
    )

    # Horizontal position at ground impact
    return solution.y_events[0][0][0]


# ------------------------------------------------------------
# Horizontal-range map R(theta, kappa)
# ------------------------------------------------------------

R = np.zeros(
    (len(kappa_values), len(theta_deg))
)

theta_opt = np.zeros(
    len(kappa_values)
)


for i, kappa in enumerate(kappa_values):

    for j, theta in enumerate(theta_rad):

        R[i, j] = quadratic_range(
            theta,
            kappa,
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
    kappa_values,
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
    kappa_values,
    R,
    levels=10,
    colors="k",
    linewidths=0.6,
    alpha=0.55,
)


# Optimal-angle curve
plt.plot(
    theta_opt,
    kappa_values,
    linestyle="--",
    linewidth=2,
    color="white",
    label=r"$\theta_{\mathrm{opt}}(\kappa)$",
)


# Axes and ticks
plt.xlabel(
    r"$\theta\ \mathrm{[deg]}$",
    fontsize=14,
)

plt.ylabel(
    r"$\kappa\ \mathrm{[m^{-1}]}$",
    fontsize=14,
)

plt.xticks(
    np.arange(15, 76, 15),
    fontsize=12,
)

plt.yticks(
    np.arange(0.0, 0.201, 0.05),
    fontsize=12,
)

plt.xlim(15.0, 75.0)
plt.ylim(0.0, 0.20)


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
    "quadratic_range_map.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "quadratic_range_map.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:




