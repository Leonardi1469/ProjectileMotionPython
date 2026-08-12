# Projectile Motion in Python

*From analytical solutions to numerical integration: A computational and pedagogical framework for projectile motion.*

---

## About this repository

This repository accompanies the article

**“From analytical solutions to numerical integration: A computational and pedagogical framework for projectile motion.”**

Its purpose is to provide a reproducible computational framework for studying projectile motion through analytical derivations, numerical integration, and Python visualizations.

Three models of increasing physical and mathematical complexity are considered:

- ideal projectile motion;
- projectile motion with linear air resistance;
- projectile motion with quadratic air resistance.

The repository is organized as a progressive study in which analytical and numerical methods are introduced according to the mathematical structure of each model.

---

## Projectile-motion models

| Model | Analytical treatment | Numerical treatment |
|:---|:---:|:---:|
| Ideal projectile motion | ✅ | ✅ |
| Linear air resistance | ✅ | ✅ |
| Quadratic air resistance | No general closed-form trajectory | ✅ |

For the ideal and linear-drag models, analytical and numerical solutions are compared directly.

For the quadratic-drag model, the equations of motion form a nonlinear coupled system, and numerical integration becomes the central computational method.

---

## Repository structure

```text
ProjectileMotionPython/
│
├── README.md
│
├── overview/
├── ideal_model/
├── linear_drag/
├── quadratic_drag/
└── comparative_analysis/
```

Each folder has a specific role in the progression of the study.

### `overview/`

Introduces the physical problem through a direct comparison of the trajectories predicted by the three projectile-motion models under identical initial conditions.

This section is intended to provide an initial visual motivation before the models are studied individually.

### `ideal_model/`

Develops the ideal projectile model, including:

- physical formulation and governing equations;
- complete analytical derivation;
- numerical formulation;
- analytical–numerical validation;
- dependence on launch angle and initial speed;
- horizontal-range map $R(v_0,\theta)$;
- optimal-angle analysis.

### `linear_drag/`

Develops projectile motion with linear air resistance, including:

- formulation of the linear drag force;
- exact analytical treatment;
- numerical formulation and analytical–numerical validation;
- ideal limit $\gamma\rightarrow0$;
- dependence on launch angle, initial speed, and $\gamma$;
- horizontal-range map $R(\theta,\gamma)$;
- optimal-angle analysis.

### `quadratic_drag/`

Develops projectile motion with quadratic air resistance, including:

- formulation of the quadratic drag force;
- nonlinear coupled equations of motion;
- numerical integration using `solve_ivp`;
- ideal limit $\kappa\rightarrow0$;
- dependence on launch angle, initial speed, and $\kappa$;
- horizontal-range map $R(\theta,\kappa)$;
- optimal-angle analysis.

### `comparative_analysis/`

Brings together the results obtained from the three models and examines their main physical differences.

This section is reserved for the final comparative analysis, including the behavior of the horizontal range $R(\theta)$ and the physical consequences of introducing linear and quadratic air resistance.

---

## Suggested reading path

The repository is designed to be explored in the following order:

$$
\boxed{\text{Overview}}
\rightarrow
\boxed{\text{Ideal model}}
\rightarrow
\boxed{\text{Linear drag}}
\rightarrow
\boxed{\text{Quadratic drag}}
\rightarrow
\boxed{\text{Comparative analysis}}.
$$

The `overview/` folder first introduces the three models visually.

The three model-specific folders then develop the physics and computational treatment in increasing order of mathematical complexity.

Finally, `comparative_analysis/` brings the results together to examine the physical consequences of the different modeling assumptions.

---

## Computational approach

The general computational workflow is:

1. formulate the governing equations;
2. derive an analytical solution when available;
3. rewrite the equations as a first-order system;
4. integrate the system numerically;
5. compare analytical and numerical results when possible;
6. explore the influence of the relevant physical parameters;
7. compare the predictions of the three models.

This approach allows numerical integration to be validated against exact results before it becomes necessary for the nonlinear quadratic-drag problem.

---

## Figures and reproducibility

All figures are generated directly from the Python programs included in the repository.

PNG files are provided for visualization on GitHub, while PDF versions are included as high-resolution outputs suitable for the associated manuscript.

A common graphical format is used throughout the repository to facilitate comparison among the different models.

---

## From analytical to numerical projectile motion

The organization of the repository reflects the increasing mathematical complexity of the physical models:

$$
\boxed{\text{Ideal}}
\rightarrow
\boxed{\text{Linear drag}}
\rightarrow
\boxed{\text{Quadratic drag}}.
$$

The ideal model admits a complete solution in elementary functions.

The linear-drag model remains analytically solvable, although its treatment introduces exponential functions and a more complex determination of characteristic quantities such as the flight time.

The quadratic-drag model leads to nonlinear coupled equations, making numerical integration the natural tool for obtaining the complete trajectory.

This progression illustrates a central idea of computational physics: analytical and numerical methods are complementary tools whose relative importance depends on the mathematical structure of the physical model.

---

## Associated article

This repository serves as supplementary computational material for the article

**“A computational and pedagogical framework for projectile motion using Python visualizations.”**

The theoretical formulations, numerical implementations, parameter studies, and figure-generation scripts provided here support the analysis developed in the manuscript.

---

© 2026 Leonardi Hernández Sánchez et al.
