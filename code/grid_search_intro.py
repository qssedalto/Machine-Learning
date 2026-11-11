"""Lesson 1: learn a one-parameter model by trying candidate values."""
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

candidates = np.linspace(0.0, 4.0, 401)
losses = []
for w in candidates:
    prediction = w * x
    mse = np.mean((prediction - y) ** 2)
    losses.append(mse)

best_index = int(np.argmin(losses))
best_w = float(candidates[best_index])
best_mse = float(losses[best_index])
new_prediction = best_w * 4.0

print(f"best w = {best_w:.1f}")
print(f"training MSE = {best_mse:.1f}")
print(f"prediction when x=4 = {new_prediction:.1f}")
assert np.isclose(best_w, 2.0)
assert np.isclose(best_mse, 0.0)
assert np.isclose(new_prediction, 8.0)
