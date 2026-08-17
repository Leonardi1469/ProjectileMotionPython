# Overview

## Initial comparison of the projectile-motion models

This section provides an initial visual comparison of the three projectile-motion models considered in this repository:

- ideal projectile motion;
- projectile motion with linear air resistance;
- projectile motion with quadratic air resistance.

The purpose of this comparison is to illustrate how different physical assumptions modify the predicted trajectory before each model is analyzed individually.

The three trajectories are computed using the same initial conditions, allowing the effect of the drag force to be identified directly.

---

## 📖 1. Three levels of physical modeling

Projectile motion can be described at different levels of approximation depending on how the interaction between the projectile and the surrounding medium is modeled.

The three cases considered here are governed by

### Ideal projectile motion

The only force acting on the projectile is gravity:

$$
\boxed{
\frac{d^2\mathbf{r}}{dt^2}
= -g\hat{\mathbf{y}}
}.
$$

In component form,

$$
\frac{d^2x}{dt^2}=0,
$$

$$
\frac{d^2y}{dt^2}=-g.
$$

This model neglects air resistance completely.

---

### Linear air resistance

The projectile experiences a resistive force proportional to its instantaneous velocity:

$$
\mathbf{F}_d=-b\mathbf{v}.
$$

Introducing

$$
\gamma=\frac{b}{m},
$$

the equation of motion becomes

$$
\boxed{
\frac{d^2\mathbf{r}}{dt^2}
=-g\hat{\mathbf{y}}
-\gamma\mathbf{v}
}.
$$

In component form,

$$
\frac{dv_x}{dt}=-\gamma v_x,
$$

$$
\frac{dv_y}{dt}=-g-\gamma v_y.
$$

The resistance increases linearly with the projectile speed.

---

### Quadratic air resistance

The resistive force is proportional to the square of the projectile speed and acts opposite to the instantaneous velocity:

$$
\mathbf{F}_d=-c|\mathbf{v}|\mathbf{v}.
$$

Introducing

$$
\kappa=\frac{c}{m},
$$

the equation of motion becomes

$$
\boxed{
\frac{d^2\mathbf{r}}{dt^2}
=-g\hat{\mathbf{y}}
-\kappa|\mathbf{v}|\mathbf{v}
}.
$$

In component form,

$$
\frac{dv_x}{dt}
=-\kappa\sqrt{v_x^2+v_y^2}\,v_x,
$$

$$
\frac{dv_y}{dt}
=-g-\kappa\sqrt{v_x^2+v_y^2}\,v_y.
$$

In this case, the horizontal and vertical velocity components are coupled through the instantaneous speed

$$
|\mathbf{v}|=\sqrt{v_x^2+v_y^2}.
$$

---

## ⚙️ 2. Common initial conditions

To make the comparison meaningful, all three models are evaluated using the same gravitational acceleration, initial speed, launch angle, and initial position.

The common initial conditions are

$$
x(0)=0,
\qquad
y(0)=0,
$$

and

$$
v_x(0)=v_0\cos(\theta),
\qquad
v_y(0)=v_0\sin(\theta).
$$

For the comparison shown below,

$$
g=9.81\ \mathrm{m/s^2},
$$

$$
v_0=20\ \mathrm{m/s},
$$

and

$$
\theta=45^\circ.
$$

For the dissipative models, representative values of the drag parameters are used:

$$
\gamma=0.2\ \mathrm{s^{-1}}
$$

for linear resistance, and

$$
\kappa=0.05\ \mathrm{m^{-1}}
$$

for quadratic resistance.

These values are used to illustrate how the inclusion and functional form of the resistive force modify the trajectory under otherwise identical launch conditions.

Because $\gamma$ and $\kappa$ have different physical dimensions and enter different force laws, their numerical values should not be interpreted as directly equivalent measures of drag strength.

---

## 💻 3. Computational comparison

The three models are evaluated within a common computational framework.

For the ideal model, the equations of motion can be solved exactly using elementary functions.

For linear resistance, the equations also admit an exact analytical treatment, although the resulting expressions contain exponential terms and are mathematically more involved.

For quadratic resistance, the velocity components become nonlinearly coupled, and the complete two-dimensional trajectory is obtained by numerical integration.

For the purpose of the comparison shown in this section, the trajectories are generated consistently from their corresponding equations of motion until the projectile returns to ground level.

The Python implementation uses a ground-impact condition defined by

$$
y(T)=0,
$$

where $T>0$ is the corresponding flight time.

This ensures that each trajectory is displayed only over its physically relevant interval of flight.

---

## 📈 4. Comparison of the three trajectories

The following figure compares the ideal, linear-drag, and quadratic-drag trajectories under the common initial conditions defined above.

![Comparison of the three projectile-motion models](three_models_comparison.png)

High-resolution PDF:

[Download PDF](three_models_comparison.pdf)

---

## 🔎 5. Initial physical observations

The figure immediately shows that the choice of physical model has a significant effect on the predicted trajectory.

The ideal model produces the largest trajectory because no mechanical energy is dissipated through aerodynamic resistance.

Its horizontal velocity remains constant:

$$
v_x=v_0\cos(\theta).
$$

Consequently, the ideal projectile continues moving horizontally without any aerodynamic reduction of its velocity during the flight.

When linear resistance is introduced, the horizontal velocity is no longer constant. Instead,

$$
v_x(t)=v_0\cos(\theta)e^{-\gamma t},
$$

so the projectile continuously loses horizontal speed.

The resulting trajectory therefore has a smaller horizontal extent than the ideal trajectory.

For quadratic resistance, the drag magnitude depends on the square of the instantaneous speed:

$$
|\mathbf{F}_d|\propto v^2.
$$

The resistance is therefore particularly sensitive to the speed of the projectile and changes continuously as the velocity changes throughout the flight.

The three trajectories consequently illustrate how progressively different assumptions about the interaction with the surrounding medium lead to different predictions even when the initial conditions are identical.

Another important visual consequence is that the dissipative trajectories are not parabolic.

The familiar parabolic trajectory is therefore not a universal property of projectile motion. It follows specifically from the ideal assumptions of constant gravitational acceleration and negligible air resistance.

---

## ❓ 6. Questions motivated by the comparison

The initial comparison raises several physical and computational questions.

For example:

- How does the launch angle modify the trajectory in each model?
- How does increasing the initial speed affect the range and maximum height?
- How does increasing air resistance modify the trajectory?
- Does the symmetry between complementary launch angles survive when drag is introduced?
- Is the classical value

$$
\theta=45^\circ
$$

still the angle that maximizes the horizontal range?
- How does the optimal launch angle change as the resistance increases?
- How different are the predictions of linear and quadratic drag?
- When can an analytical solution still be obtained?
- At what point does numerical integration become necessary?

These questions motivate the detailed study developed in the following sections of the repository.

---

## 🧭 7. Continue through the models

The three models should now be examined individually.

### Step 1 — Ideal projectile motion

Continue to:

[`../ideal_model/`](../ideal_model/)

The ideal case establishes the analytical reference model and provides the first validation of the numerical method.

---

### Step 2 — Linear air resistance

After the ideal model, continue to:

[`../linear_drag/`](../linear_drag/)

The linear-drag model introduces dissipation while preserving analytical solvability.

---

### Step 3 — Quadratic air resistance

Then continue to:

[`../quadratic_drag/`](../quadratic_drag/)

The quadratic-drag model introduces nonlinear coupling between the velocity components and motivates the use of numerical integration as the principal solution method.

---

After the three models have been studied individually, the results are brought together in:

[`../comparative_analysis/`](../comparative_analysis/)

where the physical consequences of the different modeling assumptions are examined comparatively.

---

## 🐍 8. Python code

The figure presented in this section is generated by

[`three_models_comparison.py`](three_models_comparison.py)

using NumPy, SciPy, and Matplotlib.

The corresponding PNG and PDF files are included in this folder to provide direct visualization and a high-resolution version of the figure.

---

---

## 📚 References

The theoretical, computational, and pedagogical framework implemented in this repository is supported by the following references:

1. M. Alonso and E. J. Finn, *Fundamental University Physics, Vol. 1: Mechanics*, Revised ed., Addison-Wesley, Reading, MA (1992).

2. D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, Extended, 10th ed., Wiley, Hoboken, NJ (2014).

3. J. R. Taylor, *Classical Mechanics*, University Science Books, Sausalito, CA (2005).

4. E. Brown, “Modeling theory applied: Modeling instruction in introductory physics,” *American Journal of Physics* **76** (2008) 1155. https://doi.org/10.1119/1.2983148

5. J. R. Taylor, *An Introduction to Error Analysis: The Study of Uncertainties in Physical Measurements*, 2nd ed., University Science Books, Sausalito, CA (1997).

6. C. M. Morales, J. H. Muñoz, and C. E. Vera, “Some remarks on projectile motion with a linear resistance force,” *European Journal of Physics* **44** (2023) 065003. https://doi.org/10.1088/1361-6404/acf0a5

7. F. Jobunga et al., “Analytical solution of the projectile motion under a linear drag force,” *Journal of Applied Mathematics* **2024** (2024) 8881003. https://doi.org/10.1155/2024/8881003

8. P. Chudinov, C. Ellyshev, and Y. Barykin, “Analytical construction of the projectile motion trajectory in fluid,” *Momentum* **62** (2021) 79. https://doi.org/10.29012/2005-6810-2021-62

9. F. B. Wadsworth et al., “Projectile motion: experimental datasets and classroom exercises,” *Physics Education* **60** (2025) 045024. https://doi.org/10.1088/1361-6552/adc2c5

10. F. B. Wadsworth et al., “Numerical solution of the Schrödinger equation for radiation-matter interaction using the Runge-Kutta method implemented in Python,” *Revista Mexicana de Física E* **23** (2026) 020202. https://doi.org/10.31349/RevMexFisE.23.020202

For a complete discussion of the analytical solutions, numerical implementation, parameter exploration, and pedagogical applications of the three projectile-motion models, see the accompanying manuscript.
