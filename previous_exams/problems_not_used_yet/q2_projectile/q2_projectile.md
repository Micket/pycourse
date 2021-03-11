# Question 2: Projectile motion (?p)

A projectile motion can be described by the following ordinary differential equation (ODE):

TODO: include some latex??


where `v_x`, `v_y` are velocities, and where `p_x`, `p_y` are positions, in the x- and y-diretions. ... 

Input data:

| Parameter | Value         | Description         |
|-----------|---------------|---------------------|
| m         | 0.1 kg        | projectile mass     |
| g         | 9.82 kg m/s^2 | constant of gravity |
| ...       |               |                     |


Part A (?p)
-------------

**Task:** Write a function `time_derivative(s: numpy.ndarray, t, params)` that evaluates and returns the (time) derivative of the state vector `s`, i.e. `ds/dt`.

Input:
 - `s: numpy.ndarray`: the current state vector containing `v_x`, `v_y`, `p_x` and `p_y`,
 - `t: float`: the current time,
 - `params`: problem parameters (e.g. the mass, constant of gravity, coefficient `c`).

Output:
 - A `numpy.ndarray` containing `ds/dt`.


Part B (?p)
-----------

**Task:** Write a function `simulate_projectile(c: float)` that integrates the system of equations, for the specified initial state `s0`, for (at least) 20 timesteps between `0` and `T`. Use `scipy.integrate.odeint` with the `time_derivative` function from Part A.

Input:
 - `c: float`: the coefficient for the dragforce.

Output:
- A `numpy.ndarray` containing the (integrated) state vectors for each timestep.


Part C (?p)
-----------

**Task:** Run the simulation for `c = 0`, `c = 0.001`, and `c = 0.002`. Create a *single* plot showing the three resulting flight paths. The plot must have (i) a title, (ii) x- and y-labels, and (iii) a legend that makes it clear which line corresponds to which value of `c`.


\newpage
