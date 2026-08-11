#!/usr/bin/env python
# coding: utf-8

# In[7]:


# ============================================================
# Projectile Motion in Python
# Quadratic-drag model: variation of the drag parameter kappa
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
g = 9.81                                      # m/s^2
v0 = 20.0                                     # m/s
theta_deg = 45.0                              # degrees
kappa_values = [0.0, 0.02, 0.05, 0.1, 0.2]  # 1/m

theta = np.radians(theta_deg)


# Governing equations
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


# Numerical trajectory
def numerical_trajectory(kappa):

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

    return solution.y[0], solution.y[1]


# -------- Plot --------

plt.figure(figsize=(6.8, 4.5))


# Numerical trajectories
for kappa in kappa_values:

    x_numerical, y_numerical = numerical_trajectory(kappa)

    # Continuous line: numerical solution
    plt.plot(
        x_numerical,
        y_numerical,
        linewidth=2,
        label=rf"$\kappa={kappa:.3f}\ \mathrm{{m^{{-1}}}}$",
    )


# Markers
# Not included because the quadratic-drag model is solved numerically.


# Annotations
# The case kappa = 0 corresponds to the ideal projectile model.


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
    "quadratic_kappa_variation.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "quadratic_kappa_variation.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:





# In[ ]:




