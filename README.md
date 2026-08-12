# Projectile Motion in Python

*A computational and pedagogical framework for projectile motion using Python.*

---

## About this repository

This repository accompanies the article

**“A computational and pedagogical framework for projectile motion using Python visualizations.”**

Its purpose is to provide a reproducible computational framework for studying projectile motion through analytical derivations, numerical integration, and Python visualizations.

Three models of increasing physical and mathematical complexity are considered:

- ideal projectile motion;
- projectile motion with linear air resistance;
- projectile motion with quadratic air resistance.

The progression among these models illustrates how the treatment evolves from a simple analytical solution to a nonlinear problem in which numerical integration becomes essential.

---

## Projectile-motion models

| Model | Analytical treatment | Numerical treatment |
|:---|:---:|:---:|
| Ideal projectile motion | ✅ | ✅ |
| Linear air resistance | ✅ | ✅ |
| Quadratic air resistance | No general closed-form trajectory | ✅ |

The analytical and numerical solutions are compared whenever an exact analytical treatment is available.

For the quadratic-drag model, the equations of motion are nonlinear and coupled through the instantaneous speed, so the trajectory is obtained numerically.

---

## Repository structure

```text
ProjectileMotionPython/
│
├── README.md
│
├── overview/
│
├── ideal_model/
│
├── linear_drag/
│
└── quadratic_drag/
```

### `overview/`

Provides a general comparison of the three projectile-motion models and includes:

- a direct comparison of the three trajectories under identical initial conditions;
- a comparison of the horizontal range $R(\theta)$ for the three models;
- the corresponding Python programs and publication-quality figures.

### `ideal_model/`

Contains:

- physical formulation;
- governing equations;
- complete analytical derivation;
- numerical formulation;
- analytical–numerical trajectory comparisons;
- variation of the launch angle;
- variation of the initial speed;
- horizontal-range map $R(v_0,\theta)$;
- optimal-angle analysis.

### `linear_drag/`

Contains:

- formulation of the linear drag force;
- exact analytical solution;
- numerical formulation;
- ideal limit $\gamma\rightarrow0$;
- variation of the launch angle;
- variation of the initial speed;
- variation of the drag parameter $\gamma$;
- horizontal-range map $R(\theta,\gamma)$;
- optimal-angle analysis.

### `quadratic_drag/`

Contains:

- formulation of the quadratic drag force;
- nonlinear coupled equations of motion;
- numerical integration using `solve_ivp`;
- ideal limit $\kappa\rightarrow0$;
- variation of the launch angle;
- variation of the initial speed;
- variation of the drag parameter $\kappa$;
- horizontal-range map $R(\theta,\kappa)$;
- optimal-angle analysis.

---

## Computational approach

The repository follows the same general workflow throughout the three models:

1. formulate the governing equations;
2. derive the analytical solution when available;
3. rewrite the equations as a first-order system;
4. integrate the system numerically using Python;
5. compare analytical and numerical results when possible;
6. analyze the influence of the relevant physical parameters through systematic parameter sweeps.

This progression allows the numerical method to be validated in analytically solvable cases before it is applied to the nonlinear quadratic-drag model.

---

## Figures and reproducibility

All figures presented in the repository are generated directly from the included Python programs.

PNG versions are provided for visualization within GitHub, while PDF versions are included as publication-quality outputs.

The figures are designed using a common graphical format to facilitate direct comparison among the three projectile-motion models.

---

## Repository organization by physical complexity

The project is intentionally structured as a progression:

$$
\boxed{\text{Ideal projectile}}
\rightarrow
\boxed{\text{Linear drag}}
\rightarrow
\boxed{\text{Quadratic drag}}.
$$

This progression emphasizes the transition from elementary analytical mechanics to increasingly complex analytical and computational treatments.

The final objective is not only to reproduce projectile trajectories, but also to illustrate when analytical methods remain practical, when numerical methods provide useful validation, and when numerical integration becomes necessary.

---

## Associated article

This repository serves as supplementary computational material for the article

**“A computational and pedagogical framework for projectile motion using Python visualizations.”**

The repository includes the theoretical formulation, numerical implementations, and figure-generation scripts used to support the analysis presented in the manuscript.

---

© 2026 Leonardi Hernández Sánchez et al.
