#!/usr/bin/env python
# coding: utf-8

# In[5]:


# ============================================================
# Projectile Motion in Python
# Quadratic-drag model: variation of the initial speed
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
g = 9.81                           # m/s^2
theta_deg = 45.0                   # degrees
kappa = 0.05                       # Quadratic-drag parameter c/m (1/m)
v0_values = [10, 15, 20, 25, 30] # m/s

theta = np.radians(theta_deg)


# Governing equations
# State vector: [x, y, vx, vy]
def quadratic_model(t, state):

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
def ground_event(t, state):

    if t < 1.0e-8:
        return 1.0

    return state[1]


ground_event.terminal = True
ground_event.direction = -1


# Numerical trajectory
def numerical_trajectory(v0):

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
        events=ground_event,
        max_step=0.02,
        rtol=1e-9,
        atol=1e-11,
    )

    return solution.y[0], solution.y[1]


# -------- Plot --------

plt.figure(figsize=(6.8, 4.5))


# Numerical trajectories
for v0 in v0_values:

    x_numerical, y_numerical = numerical_trajectory(v0)

    # Continuous line: numerical solution
    plt.plot(
        x_numerical,
        y_numerical,
        linewidth=2,
        label=rf"$v_0={v0}\ \mathrm{{m/s}}$",
    )


# Markers
# Not included because no analytical solution is available
# for comparison with the numerical results.


# Annotations
# The physical interpretation is discussed in the article.


# Axes and ticks
plt.xlabel(r"$x(t)\ \mathrm{[m]}$", fontsize=14)
plt.ylabel(r"$y(t)\ \mathrm{[m]}$", fontsize=14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.xlim(left=0.0)
plt.ylim(bottom=0.0)


# Legend
plt.legend(fontsize=12)
plt.grid(True, alpha=0.35)
plt.tight_layout()


# Save figure
plt.savefig(
    "quadratic_velocity_variation.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "quadratic_velocity_variation.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:




