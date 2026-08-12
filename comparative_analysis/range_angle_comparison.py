#!/usr/bin/env python
# coding: utf-8

# In[27]:


# ============================================================
# Projectile Motion in Python
# Horizontal range as a function of the launch angle
# ============================================================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import lambertw


# Plot style
mpl.rcParams["text.usetex"] = False
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.rcParams["mathtext.fontset"] = "stix"


# Physical parameters (SI units)
g = 9.81          # m/s^2
v0 = 20.0         # m/s
gamma = 0.2       # Linear-drag parameter (1/s)
kappa = 0.05      # Quadratic-drag parameter (1/m)

theta_deg = np.linspace(1.0, 89.0, 881)  # step = 0.1 deg
theta_rad = np.deg2rad(theta_deg)


# Ideal horizontal range
def ideal_range(theta):

    return (v0**2/g)*np.sin(2.0*theta)


# Linear-drag horizontal range
def linear_range(theta):

    # Auxiliary parameter
    a = 1.0 + gamma*v0*np.sin(theta)/g

    # Exact nonzero flight time using the principal Lambert-W branch
    T = (
        a
        + np.real(lambertw(-a*np.exp(-a), k=0))
    )/gamma

    # Exact horizontal range
    R = (
        v0*np.cos(theta)/gamma
        * (1.0 - np.exp(-gamma*T))
    )

    return R


# Quadratic-drag model
# State vector: [x, y, vx, vy]
def quadratic_model(t, state):

    x, y, vx, vy = state
    speed = np.hypot(vx, vy)

    return [
        vx,
        vy,
        -kappa*speed*vx,
        -g-kappa*speed*vy,
    ]


# Ground-impact event
def ground_event(t, state):

    if t < 1.0e-8:
        return 1.0

    return state[1]


ground_event.terminal = True
ground_event.direction = -1


# Quadratic-drag horizontal range
def quadratic_range(theta):

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

    # Horizontal position at ground impact
    return solution.y_events[0][0][0]


# Compute the three range curves
R_ideal = ideal_range(theta_rad)

R_linear = np.array([
    linear_range(theta)
    for theta in theta_rad
])

R_quadratic = np.array([
    quadratic_range(theta)
    for theta in theta_rad
])


# Maximum horizontal ranges
i_ideal = np.argmax(R_ideal)
i_linear = np.argmax(R_linear)
i_quadratic = np.argmax(R_quadratic)

theta_ideal = theta_deg[i_ideal]
theta_linear = theta_deg[i_linear]
theta_quadratic = theta_deg[i_quadratic]

Rmax_ideal = R_ideal[i_ideal]
Rmax_linear = R_linear[i_linear]
Rmax_quadratic = R_quadratic[i_quadratic]


# Numerical values
print("Maximum horizontal range")
print(f"Ideal:          theta = {theta_ideal:.1f} deg, R = {Rmax_ideal:.2f} m")
print(f"Linear drag:    theta = {theta_linear:.1f} deg, R = {Rmax_linear:.2f} m")
print(f"Quadratic drag: theta = {theta_quadratic:.1f} deg, R = {Rmax_quadratic:.2f} m")


# -------- Plot --------

plt.figure(figsize=(6.8, 4.5))


# Range curves
line_ideal, = plt.plot(
    theta_deg,
    R_ideal,
    linewidth=2,
    label="Ideal",
)

line_linear, = plt.plot(
    theta_deg,
    R_linear,
    linewidth=2,
    label="Linear drag",
)

line_quadratic, = plt.plot(
    theta_deg,
    R_quadratic,
    linewidth=2,
    label="Quadratic drag",
)


# Markers
plt.scatter(
    theta_ideal,
    Rmax_ideal,
    color=line_ideal.get_color(),
    s=55,
    zorder=3,
)

plt.scatter(
    theta_linear,
    Rmax_linear,
    color=line_linear.get_color(),
    s=55,
    zorder=3,
)

plt.scatter(
    theta_quadratic,
    Rmax_quadratic,
    color=line_quadratic.get_color(),
    s=55,
    zorder=3,
)


# Annotations (with values)
plt.annotate(
    rf"$\theta_{{\rm opt}}={theta_ideal:.1f}^\circ$"
    "\n"
    rf"$R_{{\max}}={Rmax_ideal:.2f}\ \mathrm{{m}}$",
    xy=(theta_ideal, Rmax_ideal),
    xytext=(-13, -57),
    textcoords="offset points",
    ha="left",
    va="bottom",
    fontsize=10.5,
    bbox=dict(
        boxstyle="round,pad=0.25",
        fc="white",
        ec="gray",
        alpha=0.9,
    ),
    arrowprops=dict(
        arrowstyle="->",
        color="gray",
        lw=1,
    ),
)

plt.annotate(
    rf"$\theta_{{\rm opt}}={theta_linear:.1f}^\circ$"
    "\n"
    rf"$R_{{\max}}={Rmax_linear:.2f}\ \mathrm{{m}}$",
    xy=(theta_linear, Rmax_linear),
    xytext=(-60, -45),
    textcoords="offset points",
    ha="left",
    va="center",
    fontsize=10.5,
    bbox=dict(
        boxstyle="round,pad=0.25",
        fc="white",
        ec="gray",
        alpha=0.9,
    ),
    arrowprops=dict(
        arrowstyle="->",
        color="gray",
        lw=1,
    ),
)

plt.annotate(
    rf"$\theta_{{\rm opt}}={theta_quadratic:.1f}^\circ$"
    "\n"
    rf"$R_{{\max}}={Rmax_quadratic:.2f}\ \mathrm{{m}}$",
    xy=(theta_quadratic, Rmax_quadratic),
    xytext=(-60, -30),
    textcoords="offset points",
    ha="left",
    va="top",
    fontsize=10.5,
    bbox=dict(
        boxstyle="round,pad=0.25",
        fc="white",
        ec="gray",
        alpha=0.9,
    ),
    arrowprops=dict(
        arrowstyle="->",
        color="gray",
        lw=1,
    ),
)


# Axes and ticks
plt.xlabel(r"$\theta\ \mathrm{[deg]}$", fontsize=14)
plt.ylabel(r"$R\ \mathrm{[m]}$", fontsize=14)

plt.xticks(
    np.arange(0, 91, 15),
    fontsize=12,
)

plt.yticks(fontsize=12)

plt.xlim(0.0, 90.0)
plt.ylim(bottom=0.0)


# Legend
plt.legend(
    fontsize=12,
    loc="upper right",
)

plt.grid(True, alpha=0.35)
plt.tight_layout()


# Save figure
plt.savefig(
    "range_angle_comparison.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "range_angle_comparison.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()


# In[ ]:




