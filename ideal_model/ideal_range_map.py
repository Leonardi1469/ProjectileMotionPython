# ============================================================
# Projectile Motion in Python
# Ideal model: horizontal range R(v0, theta)
# ============================================================

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Plot style
mpl.rcParams["text.usetex"] = False
mpl.rcParams["font.family"] = "STIXGeneral"
mpl.rcParams["mathtext.fontset"] = "stix"


# Physical constant
g = 9.81  # m/s^2


# Parameter grids
theta_deg = np.linspace(15.0, 75.0, 500)   # degrees
v0_values = np.linspace(10.0, 40.0, 500)   # m/s


# Mesh: X-axis = theta, Y-axis = v0
TH, V0 = np.meshgrid(
    np.deg2rad(theta_deg),
    v0_values,
)


# Horizontal range
# R = v0^2 sin(2 theta) / g
R = (V0**2/g)*np.sin(2.0*TH)


# Optimal launch angle
theta_opt = 45.0  # degrees


# -------- Plot --------

plt.figure(figsize=(6.8, 4.5))


# Filled contour
# Color represents the horizontal range
cs = plt.contourf(
    theta_deg,
    v0_values,
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
    v0_values,
    R,
    levels=10,
    colors="k",
    linewidths=0.6,
    alpha=0.55,
)


# Optimal-angle line
plt.axvline(
    theta_opt,
    linestyle="--",
    linewidth=2,
    color="white",
    label=r"$\theta_{\mathrm{opt}}=45^\circ$",
)


# Axes and ticks
plt.xlabel(
    r"$\theta\ \mathrm{[deg]}$",
    fontsize=14,
)

plt.ylabel(
    r"$v_0\ \mathrm{[m/s]}$",
    fontsize=14,
)

plt.xticks(
    np.arange(15, 76, 15),
    fontsize=12,
)

plt.yticks(
    np.arange(10, 41, 10),
    fontsize=12,
)

plt.xlim(15.0, 75.0)
plt.ylim(10.0, 40.0)


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
    "ideal_range_map.png",
    dpi=400,
    bbox_inches="tight",
)

plt.savefig(
    "ideal_range_map.pdf",
    dpi=400,
    bbox_inches="tight",
)

plt.show()
