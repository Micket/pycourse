import numpy as np
from scipy.optimize import linprog

# Part A
"""
The objective function is the profit, it is stated to be: f(x, y) = 50 * x + 40 * y

Constraints: (using unit m^2 for cotton and polyester)
    Cotton:     Each pair of pants require 1 and each jacket requires 1.5.
                In total this should be less than what is available (750): 1 * x + 1.5 * y <= 750
    Polyester:  Each pair of pants require 2 and each jacket requires 1.
                In total this should be less than what is available (1000): 2 * x + 1 * y <= 1000

    Pants:      Must be positive: x >= 0
    jackets:    Must be positive: y >= 0
"""


# Part B
"""
In scipy.optimize linprog is a minimisation problem, and all constraints are <=, i.e. we need to rewrite by multiplying for example
  the objective function by -1 

The problem need to be formulated on the form:
 find x to minimise c^T * X
 where A_ub * X <= b_ub, A_eq * X = b_eq and L < X < U

 Translating our data into this we get:
 c = [-50, -40]^T
 A_ub = [1, 1.5;
         2, 1]
b_ub = [750, 1000]^T

We do not have any equality constraints.

L = [0, 0]^T, U = [infinity, infinity] (we can use None for U)

"""

c = np.array([-50, -40])
A_ub = np.array([[1.0, 1.5],
                 [2.0, 1.0]])
b_ub = np.array([750, 1000])
bounds = [(0, None), (0, None)] # Lower and Upper bounds on x and y

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
# print(result)
x, y = result.x
print(f"No. of pants: {round(x)}, no. of jackets: {round(y)}, total sales value: {50 * round(x) + 40 * round(y)}")
