"""Verify a binary logistic regression gradient by central differences."""
import numpy as np

X = np.array([[1.0, 1.0], [2.0, 1.0], [-1.0, 1.0], [0.5, 1.0]])
y = np.array([1.0, 1.0, 0.0, 0.0])
beta = np.array([0.4, -0.2])

def objective(b):
    z = X @ b
    # logaddexp gives a stable average negative log-likelihood.
    return np.mean(np.logaddexp(0.0, z) - y * z)

def analytic_gradient(b):
    z = X @ b
    probability = 1 / (1 + np.exp(-z))
    return X.T @ (probability - y) / len(y)

h = 1e-5
numerical = np.empty_like(beta)
for j in range(len(beta)):
    step = np.zeros_like(beta)
    step[j] = h
    numerical[j] = (objective(beta + step) - objective(beta - step)) / (2 * h)

analytic = analytic_gradient(beta)
print("Analytic gradient :", analytic)
print("Numerical gradient:", numerical)
print("Max abs difference:", np.max(np.abs(analytic - numerical)))
