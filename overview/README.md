# Projectile Motion in Python

## Overview

This repository accompanies the article

> **A computational and pedagogical framework for projectile motion using Python visualizations.**

Its purpose is to provide a reproducible computational framework for studying projectile motion through analytical solutions, numerical simulations, and Python visualizations. The repository is organized as a companion resource to the article, allowing readers to reproduce every figure presented in the manuscript while exploring the corresponding theoretical and computational developments.

Three projectile-motion models with increasing mathematical and computational complexity are considered throughout this repository.

---

## Projectile-motion models

| Model | Analytical solution | Numerical solution |
|:------|:-------------------:|:------------------:|
| Ideal projectile motion | ✅ | ✅ |
| Linear air resistance | ✅ | ✅ |
| Quadratic air resistance | ❌ | ✅ |

The progression from the ideal model to quadratic air resistance illustrates how increasing physical realism also increases the mathematical complexity of the problem. While the first two models admit analytical solutions, the quadratic-drag model generally requires numerical integration.

---

## Comparison of the three projectile-motion models

The figure below compares the trajectories predicted by the three projectile-motion models using identical initial conditions. It provides an overview of how air resistance progressively modifies the projectile trajectory.

![Comparison of the three projectile-motion models](three_models_comparison.png)

The ideal model produces the familiar parabolic trajectory. When a drag force proportional to the velocity is included, the trajectory departs from a parabola but still admits an analytical solution. In contrast, the quadratic-drag model generally has no closed-form analytical solution, making numerical methods essential for describing the projectile motion.

---

## 🐍 Python code

| Program | Description |
|:--------|:------------|
| `three_models_comparison.py` | Generates the comparison figure of the three projectile-motion models using identical initial conditions. |

---

## 📄 High-resolution figure

The publication-quality version of the comparison figure is available below.

[Download PDF](three_models_comparison.pdf)

---

## Repository organization

The repository is organized according to the projectile-motion model being studied.

| Folder | Contents |
|:------|:---------|
| `ideal_model` | Ideal projectile motion. |
| `linear_drag` | Projectile motion with linear air resistance. |
| `quadratic_drag` | Projectile motion with quadratic air resistance. |

Each folder contains:

- the physical description of the model;
- the governing differential equations;
- the analytical solution (when available);
- the numerical formulation;
- the documented Python implementation;
- the figures reproduced in the accompanying article.

Together, these folders provide a complete computational framework for reproducing all the results presented in the manuscript.

---

## 📚 References

The references associated with this overview will be incorporated after the accompanying manuscript is finalized.
