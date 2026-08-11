#!/usr/bin/env python
# coding: utf-8

# In[5]:


# ============================================================
# Projectile Motion in Python
# Linear-drag model: variation of the launch angle
# ============================================================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


# Plot style
mpl.rcParams["text.usetex"] = False
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.rcParams["mathtext.fontset"] = "stix"


# Physical parameters (SI units)
g = 9.81                              # m/s^2
v0 = 20.0                             # m/s
gamma = 0.2                          # Linear-drag parameter b/m (1/s)
theta_values = [15, 30, 45, 60, 75] # degrees


# Governing equations
# State vector: [x, y, vx, vy]
def linear_model(t, state):

    x, y, vx, vy = state

    return [
        vx,
        vy,
        -gamma*vx,
        -g-gamma*vy,
    ]


# Ground-impact event
# The integration stops when the projectile returns to y = 0.
def ground_event(t, state):

    if t < 1.0e-8:
        return 1.0

    return state[1]


ground_event.terminal = True
ground_event.direction = -1


# Analytical trajectory
def analytical_trajectory(theta):

    # Exact vertical position
    def y_exact(t):
        return (
            (v0*np.sin(theta) + g/gamma)
            * (1.0 - np.exp(-gamma*t))/gamma
            - (g/gamma)*t
        )

    # Nonzero root of y(t) = 0 gives the flight time
    T_ideal = 2.0*v0*np.sin(theta)/g
    T = brentq(y_exact, 1.0e-8, 2.0*T_ideal + 2.0)

    # Time coordinates
    t = np.linspace(0.0, T, 300)

    # Exact parametric solution
    x = (
        v0*np.cos(theta)/gamma
        * (1.0 - np.exp(-gamma*t))
    )

    y = (
        (v0*np.sin(theta) + g/gamma)
        * (1.0 - np.exp(-gamma*t))/gamma
        - (g/gamma)*t
    )

    return x, y


# Numerical trajectory
def numerical_trajectory(theta):

    # Initial conditions
    state0 = [
        0.0,
        0.0,
        v0*np.cos(theta),
        v0*np.sin(theta),
    ]

    solution = solve_ivp(
        linear_model,
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


# Analytical and numerical trajectories
for theta_deg in theta_values:

    theta = np.radians(theta_deg)

    x_analytical, y_analytical = analytical_trajectory(theta)
    x_numerical, y_numerical = numerical_trajectory(theta)

    # Continuous line: analytical solution
    line, = plt.plot(
        x_analytical,
        y_analytical,
        linewidth=2,
        label=rf"$\theta={theta_deg}^\circ$",
    )

    # Circular markers: numerical solution
    plt.plot(
        x_numerical,
        y_numerical,
        linestyle="none",
        marker="o",
        markersize=4,
        markevery=10,
        color=line.get_color(),
    )


# Markers
# Circular markers represent the numerical results.


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
    "linear_angle_variation.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "linear_angle_variation.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:




