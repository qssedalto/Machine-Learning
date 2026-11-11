"""Lesson 2: turn the ordinary least squares formulas into code."""
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([2.0, 3.0, 5.0, 4.0])

x_mean = float(np.mean(x))
y_mean = float(np.mean(y))
numerator = float(np.sum((x - x_mean) * (y - y_mean)))
denominator = float(np.sum((x - x_mean) ** 2))
assert denominator > 0.0, "Cannot identify slope when all x are equal."

w = numerator / denominator
b = y_mean - w * x_mean
prediction = w * x + b
mse = float(np.mean((prediction - y) ** 2))

print(f"mean x = {x_mean:.1f}, mean y = {y_mean:.1f}")
print(f"w = {w:.1f}, b = {b:.1f}")
print(f"training MSE = {mse:.2f}")
print(f"prediction when x=5 = {w * 5.0 + b:.1f}")
assert np.isclose(w, 0.8)
assert np.isclose(b, 1.5)
assert np.isclose(mse, 0.45)
