"""Compare analytic least squares and full-batch gradient descent."""
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])
X = np.column_stack([x, np.ones_like(x)])
m = len(y)

# The coefficient order is [slope, intercept].
beta_lstsq, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Minimize J(beta) = ||X @ beta - y||^2 / (2 * m).
eta = 0.1
beta = np.zeros(2)
for iteration in range(5000):
    error = X @ beta - y
    gradient = X.T @ error / m
    beta = beta - eta * gradient

predicted = X @ beta
mse = np.mean((predicted - y) ** 2)

print("Analytic LS :", beta_lstsq)
print("Gradient GD :", beta)
print("MSE         :", mse)
print("Exact MSE   :", 1 / 18)
