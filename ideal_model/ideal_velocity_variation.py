# ============================================================
# Projectile Motion in Python
# Ideal projectile model: variation of the initial speed
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
g = 9.81                          # m/s^2
theta_deg = 45.0                  # degrees
v0_values = [10, 15, 20, 25, 30] # m/s

theta = np.radians(theta_deg)


# Governing equations
# State vector: [x, y, vx, vy]
def ideal_model(t, state):

    x, y, vx, vy = state

    return [
        vx,
        vy,
        0.0,
        -g,
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
def analytical_trajectory(v0):

    # Horizontal range
    R = (v0**2/g)*np.sin(2.0*theta)

    # Horizontal coordinates
    x = np.linspace(0.0, R, 300)

    # Cartesian trajectory y(x)
    y = (
        x*np.tan(theta)
        - (g*x**2)/(2.0*v0**2*np.cos(theta)**2)
    )

    return x, y


# Numerical trajectory
def numerical_trajectory(v0):

    # Initial conditions
    state0 = [
        0.0,
        0.0,
        v0*np.cos(theta),
        v0*np.sin(theta),
    ]

    # Analytical flight time used only to define the time interval
    T = 2.0*v0*np.sin(theta)/g

    solution = solve_ivp(
        ideal_model,
        (0.0, 1.1*T),
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
for v0 in v0_values:

    x_analytical, y_analytical = analytical_trajectory(v0)
    x_numerical, y_numerical = numerical_trajectory(v0)

    # Continuous line: analytical solution
    line, = plt.plot(
        x_analytical,
        y_analytical,
        linewidth=2,
        label=rf"$v_0={v0}\ \mathrm{{m/s}}$",
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
    "ideal_velocity_variation.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "ideal_velocity_variation.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()
