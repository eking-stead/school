import numpy as np

# Coefficient matrix
A = np.array([
    [1, 0.7, 0.9],
    [0, 0.4, 0],
    [0, 0, 0.15]
])

# Right-hand side
b = np.array([120, 32, 18])

# Solve the system
solution = np.linalg.solve(A, b)

P, I, C = solution

print(f"P = {P}")
print(f"I = {I}")
print(f"C = {C}")
