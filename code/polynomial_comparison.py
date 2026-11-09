"""Reproducible degree-comparison experiment for polynomial regression."""
import numpy as np

rng = np.random.default_rng(20261109)
train_x = np.sort(rng.uniform(0, 1, 28))
test_x = np.linspace(0, 1, 400)


def true_function(x):
    return np.sin(2 * np.pi * x)


train_y = true_function(train_x) + rng.normal(0, 0.18, len(train_x))
test_y = true_function(test_x) + rng.normal(0, 0.18, len(test_x))

for degree in (1, 3, 5, 8, 10):
    # Polynomial.fit rescales the input domain before fitting.
    poly = np.polynomial.Polynomial.fit(train_x, train_y, deg=degree)
    train_mse = np.mean((poly(train_x) - train_y) ** 2)
    test_mse = np.mean((poly(test_x) - test_y) ** 2)
    print(f"degree={degree:2d}, train MSE={train_mse:.6f}, test MSE={test_mse:.6f}")
