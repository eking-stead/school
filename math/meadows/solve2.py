import numpy as np
from scipy.optimize import linprog

# Objective function (negated because linprog minimizes)
c = [-1.5, -2.0, -2.25] # Profit for plain / iced / chocolate

# Inequality constraint matrix
A = [
    [1, 0.7, 0.9],   # dough per dozen for Plain / iced / chocolate
    [0, 0.4, 0],     # icing per dozen for Plain / iced / chocolate
    [0, 0, 0.15]     # chocolate chips per dozen for Plain / iced / chocolate
]

b = [120, 32, 18] # Total amount of Dough / icing / chocolate chips

# Bounds (nonnegative)
bounds = [(0, None), (0, None), (0, None)]

# Solve
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

P, I, C = result.x
max_profit = -result.fun

print(f"P (plain dozens): {P}")
print(f"I (iced dozens): {I}")
print(f"C (choc chip dozens): {C}")
print(f"Maximum Profit: ${max_profit}")
