# Comparative Analysis

## Physical interpretation across the three projectile-motion models

This section brings together the results obtained from the three projectile-motion models studied in this repository:

- ideal projectile motion;
- projectile motion with linear air resistance;
- projectile motion with quadratic air resistance.

The purpose is not to repeat the derivations developed in the individual model folders, but to compare their physical predictions and answer the questions raised in the initial [`overview/`](../overview/).

The comparison highlights a central idea:

> Familiar results from elementary projectile motion, such as the parabolic trajectory, complementary-angle symmetry, and the optimal launch angle of $45^\circ$, arise from the assumptions of the ideal model and should not be interpreted as universal properties of projectile motion.

---

## 📖 1. Reference case

To compare the three models directly, the horizontal range is calculated as a function of the launch angle while the initial speed is fixed at

$$
\boxed{
v_0=20.0\ \mathrm{m/s}
}.
$$

For the dissipative models, the reference parameters are

$$
\boxed{
\gamma=0.2\ \mathrm{s^{-1}}
}
$$

for linear drag, and

$$
\boxed{
\kappa=0.05\ \mathrm{m^{-1}}
}
$$

for quadratic drag.

The launch angle $\theta$ is varied while these quantities remain fixed.

It is important to emphasize that $\gamma$ and $\kappa$ belong to different drag laws and have different physical dimensions. Their numerical values therefore do **not** represent equivalent measures of aerodynamic resistance.

Consequently, the numerical values of the maximum range and optimal launch angle reported below correspond specifically to this reference case. They should not be interpreted as universal values for the linear- and quadratic-drag models.

The broader dependence on the model parameters is explored through the parameter maps presented in the individual model folders.

---

## 📈 2. Horizontal range and optimal launch angle

The following figure compares the horizontal range $R(\theta)$ predicted by the three models.

![Horizontal range as a function of launch angle](range_angle_comparison.png)

High-resolution PDF:

[Download PDF](range_angle_comparison.pdf)

For the reference conditions considered here, the maxima are

| Model | $\theta_{\mathrm{opt}}$ | $R_{\max}$ |
|:---|---:|---:|
| Ideal | $45.0^\circ$ | $40.77\ \mathrm{m}$ |
| Linear drag | $40.4^\circ$ | $29.45\ \mathrm{m}$ |
| Quadratic drag | $38.7^\circ$ | $17.83\ \mathrm{m}$ |

Two effects are immediately visible.

First, the presence of air resistance reduces the horizontal range relative to the ideal prediction.

Second, the maximum of $R(\theta)$ is displaced toward angles below $45^\circ$ for the dissipative cases considered here.

Thus, introducing air resistance changes not only how far the projectile travels, but also the launch condition that maximizes that distance.

---

## 🔎 3. How large is the reduction in range?

The ideal model provides the reference maximum range

$$
R_{\max}^{\mathrm{ideal}}
= 40.77\ \mathrm{m}.
$$

For the linear-drag case,

$$
\frac{R_{\max}^{\mathrm{linear}}}
{R_{\max}^{\mathrm{ideal}}}
= \frac{29.45}{40.77}
\approx
0.722.
$$

Thus, under the selected conditions, the projectile reaches approximately

$$
\boxed{72.2\%}
$$

of the ideal maximum range, corresponding to a reduction of approximately

$$
\boxed{27.8\%}.
$$

For the quadratic-drag case,

$$
\frac{R_{\max}^{\mathrm{quadratic}}}
{R_{\max}^{\mathrm{ideal}}}
= \frac{17.83}{40.77}
\approx
0.437.
$$

The corresponding range is therefore approximately

$$
\boxed{43.7\%}
$$

of the ideal maximum, representing a reduction of approximately

$$
\boxed{56.3\%}.
$$

These results can be summarized as

| Model | $R_{\max}$ | $R_{\max}/R_{\max}^{\mathrm{ideal}}$ | Reduction |
|:---|---:|---:|---:|
| Ideal | $40.77\ \mathrm{m}$ | $1.000$ | $0\%$ |
| Linear drag | $29.45\ \mathrm{m}$ | $0.722$ | $27.8\%$ |
| Quadratic drag | $17.83\ \mathrm{m}$ | $0.437$ | $56.3\%$ |

These percentages characterize the particular reference conditions used in the figure.

In particular, the stronger reduction observed for the quadratic-drag curve should **not** be interpreted as a universal quantitative comparison between linear and quadratic drag. The two models contain different parameters, with different dimensions and different physical meanings.

---

## 🎯 4. Why is $45^\circ$ special in the ideal model?

For a projectile launched and landing at the same height, the ideal horizontal range is

$$
R_{\mathrm{ideal}}(\theta)
=
\frac{v_0^2}{g}\sin(2\theta).
$$

At fixed $v_0$, maximizing the range is equivalent to maximizing

$$
\sin(2\theta).
$$

Since its maximum value occurs when

$$
2\theta=90^\circ,
$$

the optimal launch angle is

$$
\boxed{
\theta_{\mathrm{opt}}^{\mathrm{ideal}}
=
45^\circ
}.
$$

An important consequence is that this result does not depend on $v_0$ under the assumptions of the ideal model.

The familiar statement that a projectile achieves maximum range at $45^\circ$ is therefore not a universal law of projectile motion. It follows from a specific set of assumptions: uniform gravity, negligible air resistance, and equal launch and landing heights.

---

## 🔄 5. What happens to complementary launch angles?

Another characteristic property of the ideal model follows from

$$
R_{\mathrm{ideal}}(\theta)
=
\frac{v_0^2}{g}\sin(2\theta).
$$

Because

$$
\sin(2\theta)
=
\sin\left[2(90^\circ-\theta)\right],
$$

the ideal range satisfies

$$
\boxed{
R_{\mathrm{ideal}}(\theta)
=
R_{\mathrm{ideal}}(90^\circ-\theta)
}.
$$

Therefore, complementary angles such as

$$
30^\circ
\qquad\text{and}\qquad
60^\circ
$$

produce the same horizontal range in the ideal model.

This symmetry is clearly reflected in the ideal $R(\theta)$ curve, whose maximum occurs at its symmetry point,

$$
\theta=45^\circ.
$$

When velocity-dependent drag is introduced, this simple symmetry is generally lost.

A low-angle and a high-angle trajectory no longer experience dynamically equivalent motion. Their flight times, horizontal velocity histories, and cumulative exposure to the resistive force differ.

Consequently, in the dissipative models,

$$
R(\theta)
$$

is generally not symmetric about $45^\circ$.

The displacement of the maxima observed in the figure is one manifestation of this broken ideal symmetry.

---

## 🎯 6. Does the optimal angle remain $45^\circ$ when drag is present?

For the reference case shown in the figure,

$$
\theta_{\mathrm{opt}}^{\mathrm{ideal}}
=
45.0^\circ,
$$

whereas

$$
\theta_{\mathrm{opt}}^{\mathrm{linear}}
=
40.4^\circ
$$

and

$$
\theta_{\mathrm{opt}}^{\mathrm{quadratic}}
=
38.7^\circ.
$$

Relative to the ideal value, the shifts are

$$
\Delta\theta_{\mathrm{linear}}
=
45.0^\circ-40.4^\circ
=
\boxed{4.6^\circ},
$$

and

$$
\Delta\theta_{\mathrm{quadratic}}
=
45.0^\circ-38.7^\circ
=
\boxed{6.3^\circ}.
$$

These particular values depend on the selected parameters.

More generally, the optimal angle in the dissipative models should be regarded as a parameter-dependent quantity:

$$
\boxed{
\theta_{\mathrm{opt}}^{\mathrm{linear}}
=
\theta_{\mathrm{opt}}(v_0,\gamma)
}
$$

and

$$
\boxed{
\theta_{\mathrm{opt}}^{\mathrm{quadratic}}
=
\theta_{\mathrm{opt}}(v_0,\kappa)
}.
$$

This is fundamentally different from the ideal result, for which

$$
\theta_{\mathrm{opt}}=45^\circ
$$

under equal launch and landing heights regardless of the value of $v_0$.

---

## 💨 7. Why can drag favor lower launch angles?

The physical origin of the shift can be understood from the competition between horizontal motion and flight time.

The initial velocity components are

$$
v_{0x}=v_0\cos(\theta),
$$

and

$$
v_{0y}=v_0\sin(\theta).
$$

Increasing the launch angle increases the initial vertical component but decreases the initial horizontal component.

In the ideal model, a larger vertical component produces a longer flight time without any penalty from aerodynamic dissipation. The balance between horizontal velocity and flight time leads exactly to the optimum at $45^\circ$.

With air resistance, a longer flight also means that the resistive force acts over a longer interval. At the same time, the horizontal velocity continuously decreases.

Therefore, the balance that produces the ideal $45^\circ$ result is altered.

For the dissipative cases explored here, this competition shifts the maximum horizontal range toward lower launch angles.

The physical interpretation is therefore not simply that "drag reduces the range." Drag modifies the optimization problem itself.

---

## 🗺️ 8. What do the parameter sweeps tell us beyond this reference case?

The $R(\theta)$ comparison shown above is a representative cross-section of a larger parameter space.

It should therefore be interpreted together with the parameter maps developed for the individual models.

For the ideal model, the range map is

$$
\boxed{
R=R(v_0,\theta)
}.
$$

It shows how the range changes simultaneously with initial speed and launch angle.

For linear drag, the corresponding map is

$$
\boxed{
R=R(\theta,\gamma)
}
$$

at fixed initial speed.

For quadratic drag,

$$
\boxed{
R=R(\theta,\kappa)
}
$$

is examined under the same type of fixed-$v_0$ analysis.

These maps provide information that cannot be obtained from a single trajectory.

They show that the range is part of a continuous parameter landscape rather than an isolated numerical result.

In particular, they allow the reader to see how changing the drag parameter modifies the dependence of the range on launch angle and how the region associated with maximum range evolves.

The final $R(\theta)$ figure should therefore be interpreted as a **representative cross-section of the broader parameter space explored in the individual model folders**, rather than as a universal quantitative comparison between the two drag laws.

This distinction is important when interpreting the numerical values reported in the previous sections.

---

## 🚀 9. What does changing the initial speed teach us?

The trajectory studies performed for the three models also reveal the role of the initial speed.

In the ideal model,

$$
R_{\mathrm{ideal}}
=
\frac{v_0^2}{g}\sin(2\theta),
$$

and therefore, for fixed $\theta$,

$$
\boxed{
R_{\mathrm{ideal}}\propto v_0^2
}.
$$

The dependence is simple and known exactly.

When drag is introduced, increasing $v_0$ has two competing consequences.

The projectile begins with more kinetic energy and can potentially travel farther, but the resistive force also becomes larger because it depends on the instantaneous speed.

For linear drag,

$$
|\mathbf{F}_d|\propto v,
$$

whereas for quadratic drag,

$$
|\mathbf{F}_d|\propto v^2.
$$

Thus, the effect of increasing $v_0$ is no longer described by the simple ideal scaling.

This illustrates another important modeling lesson: a parameter that produces a simple scaling law in an ideal model can acquire a more complex role when additional physical interactions are included.

---

## 🌬️ 10. Linear and quadratic drag are not interchangeable

Both dissipative models introduce a force opposite to the direction of motion, but their physical and mathematical structures are different.

For linear drag,

$$
\mathbf{F}_d=-b\mathbf{v},
$$

so that

$$
|\mathbf{F}_d|\propto v.
$$

For quadratic drag,

$$
\mathbf{F}_d=-c|\mathbf{v}|\mathbf{v},
$$

and therefore

$$
|\mathbf{F}_d|\propto v^2.
$$

The normalized parameters

$$
\gamma=\frac{b}{m}
$$

and

$$
\kappa=\frac{c}{m}
$$

also have different dimensions:

$$
[\gamma]=\mathrm{s^{-1}},
$$

whereas

$$
[\kappa]=\mathrm{m^{-1}}.
$$

Consequently, the values of $\gamma$ and $\kappa$ cannot be compared directly as though they represented the same amount of resistance.

The purpose of comparing the two models is instead to investigate how different assumptions about the velocity dependence of the resistive force modify the trajectory and the resulting physical predictions.

---

## 🧮 11. From analytical to numerical modeling

One of the central features of this project is the progressive change in mathematical complexity across the three models.

### Ideal projectile motion

The equations are uncoupled and the acceleration is constant.

The complete trajectory can be obtained analytically using elementary functions.

At the same time, numerical integration can reproduce the exact trajectory, providing a direct validation of the computational implementation.

### Linear air resistance

The equations remain analytically solvable, but the solution now contains exponential functions.

The analytical and numerical trajectories can again be compared directly.

This provides a second validation problem, now involving dissipative dynamics.

### Quadratic air resistance

The horizontal and vertical equations contain the instantaneous speed

$$
v=\sqrt{v_x^2+v_y^2},
$$

which couples the velocity components nonlinearly.

The system takes the form

$$
\frac{dv_x}{dt}
=
-\kappa v v_x,
$$

$$
\frac{dv_y}{dt}
=
-g-\kappa v v_y.
$$

For the complete two-dimensional problem considered here, a general closed-form trajectory suitable for the same direct analytical treatment is not available.

Numerical integration therefore becomes the practical method for obtaining the motion.

The progression can be summarized as

$$
\boxed{
\text{Ideal}
\rightarrow
\text{Linear drag}
\rightarrow
\text{Quadratic drag}
}
$$

and mathematically as

$$
\boxed{
\text{elementary analytical solution}
\rightarrow
\text{more involved analytical solution}
\rightarrow
\text{nonlinear numerical solution}
}.
$$

---

## 💻 12. Why use numerical methods even when an analytical solution exists?

The computational approach is useful before it becomes mathematically necessary.

For the ideal model, the numerical solution can be compared with a simple exact solution.

For linear drag, it can be compared with a more involved exact solution.

Agreement in these two analytically solvable cases provides confidence in the numerical procedure before it is applied to the quadratic-drag problem.

Numerical computation also enables systematic parameter exploration.

Instead of studying only isolated trajectories, the same computational framework can be used to investigate

$$
R(v_0,\theta),
$$

$$
R(\theta,\gamma),
$$

and

$$
R(\theta,\kappa).
$$

The role of computation is therefore twofold:

1. **validation**, when an analytical benchmark exists;
2. **exploration and solution**, when the parameter space becomes large or the equations no longer admit the same analytical treatment.

Analytical and numerical approaches are therefore complementary rather than competing descriptions.

---

## ❓ 13. Answers to the questions raised in the overview

The initial [`overview/`](../overview/) introduced several questions that can now be answered using the results of the three models.

### How does the launch angle modify the trajectory?

The launch angle determines how the initial speed is distributed between horizontal and vertical motion. This controls the competition between horizontal displacement and flight time. With drag, the same competition is additionally affected by velocity-dependent dissipation.

### How does increasing the initial speed affect the motion?

Increasing $v_0$ generally increases the characteristic distances reached by the projectile. In the ideal model the dependence follows a simple quadratic scaling for the range, whereas drag modifies this behavior because the resistive force itself depends on speed.

### How does air resistance modify the trajectory?

Air resistance reduces the projectile velocity during flight, decreases the horizontal range, changes the shape of the trajectory, and modifies the conditions that maximize the range.

### Does the symmetry between complementary launch angles survive?

It is exact in the ideal model for equal launch and landing heights, but it is generally lost when velocity-dependent resistance is introduced.

### Is $45^\circ$ always the optimal launch angle?

No.

It is the optimal angle for the ideal model under the assumptions considered here. In dissipative motion, the optimum depends on the parameters defining the problem.

### How does the optimal angle change when resistance is introduced?

For the reference cases studied here, the optimum shifts below $45^\circ$.

The exact value depends on the initial speed and on the corresponding drag parameter.

### Are linear and quadratic drag equivalent?

No.

They represent different physical dependences of the resistive force on speed and involve parameters with different physical dimensions.

### When does numerical integration become necessary?

For the progression studied here, numerical integration becomes essential for the complete quadratic-drag problem, where the horizontal and vertical velocity equations are nonlinearly coupled.

---

## 🎓 14. Pedagogical significance

Projectile motion is commonly introduced as one of the first applications of Newton's second law because the ideal problem leads to a simple analytical solution.

That simplicity makes it an excellent starting point, but it can also create the impression that familiar results such as a parabolic trajectory or an optimal angle of $45^\circ$ are intrinsic properties of all projectile motion.

The progression developed in this repository provides an opportunity to examine that assumption critically.

Students begin with a model in which the governing equations can be solved exactly and the physical predictions are transparent.

They then introduce a linear resistive force. The physics becomes more realistic, the mathematical treatment becomes more involved, but an analytical solution is still available. Numerical integration can therefore be compared directly with the exact result.

Finally, quadratic resistance changes the mathematical structure of the problem. The velocity components become nonlinearly coupled, and numerical integration becomes the natural computational tool.

A single physical problem therefore connects several important concepts:

- Newton's second law;
- model assumptions and approximations;
- ordinary differential equations;
- analytical solutions;
- numerical integration;
- validation of computational methods;
- parameter exploration;
- optimization;
- scientific visualization;
- and physical interpretation.

This progression also helps students understand **why numerical methods are introduced**.

Numerical computation is not used simply because a computer is available. It first provides an independent way to reproduce known analytical results and then becomes necessary when the mathematical structure of the model prevents the same type of closed-form treatment.

The transition

$$
\boxed{
\text{analytical}
\rightarrow
\text{analytical + numerical}
\rightarrow
\text{numerical}
}
$$

can therefore be observed within a single familiar mechanics problem.

This makes projectile motion a useful pedagogical bridge between introductory mechanics and computational physics.

---

## 🧠 15. Main physical conclusions

The comparison of the three models leads to several central conclusions.

1. The parabolic trajectory is a consequence of the ideal approximation and is not preserved when velocity-dependent air resistance is included.

2. Air resistance reduces the horizontal range relative to the corresponding ideal prediction.

3. The complementary-angle symmetry of the ideal model is generally lost in dissipative motion.

4. The familiar result

   $$
   \theta_{\mathrm{opt}}=45^\circ
   $$

   is not universal. For dissipative motion, the optimal angle depends on the physical parameters of the problem.

5. For the specific reference conditions

   $$
   v_0=20.0\ \mathrm{m/s},
   \qquad
   \gamma=0.2\ \mathrm{s^{-1}},
   \qquad
   \kappa=0.05\ \mathrm{m^{-1}},
   $$

   the optimal angles are

   $$
   45.0^\circ,\qquad
   40.4^\circ,\qquad
   38.7^\circ
   $$

   for the ideal, linear-drag, and quadratic-drag models, respectively.

6. The corresponding maximum ranges for this reference case are

   $$
   40.77\ \mathrm{m},
   \qquad
   29.45\ \mathrm{m},
   \qquad
   17.83\ \mathrm{m}.
   $$

   These numerical values characterize the selected parameter set and are not universal properties of the drag models.

7. Linear and quadratic drag represent different physical assumptions and cannot be compared solely through the numerical values of $\gamma$ and $\kappa$.

8. The parameter maps show that a single trajectory or a single set of parameters provides only one view of the problem. Computational exploration makes it possible to study how the physical predictions evolve across parameter space.

9. Analytical solutions remain valuable even when numerical methods are available because they provide physical insight and benchmarks for validating the computational implementation.

10. The quadratic-drag model illustrates the point at which numerical integration becomes the practical route for studying the complete trajectory within the progression considered here.

Taken together, these results illustrate a broader lesson:

> Increasing the physical realism of a model can change not only its quantitative predictions, but also its mathematical structure and the methods required to study it.

---

## 🐍 16. Python code and figure files

The comparative analysis shown in this section is generated by

[`range_angle_comparison.py`](range_angle_comparison.py)

with graphical outputs

- [`range_angle_comparison.png`](range_angle_comparison.png)
- [`range_angle_comparison.pdf`](range_angle_comparison.pdf)

The broader parameter studies used to support the interpretation presented here are available in:

- [`../ideal_model/`](../ideal_model/)
- [`../linear_drag/`](../linear_drag/)
- [`../quadratic_drag/`](../quadratic_drag/)

---

## 🔙 Repository home

Return to the main repository:

[`../README.md`](../README.md)

---
