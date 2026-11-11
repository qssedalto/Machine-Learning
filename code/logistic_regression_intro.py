"""Lesson 4: one SGD step for a one-sample logistic regression."""
from math import exp, log


def sigmoid(z):
    return 1.0 / (1.0 + exp(-z))


x, y = 2.0, 1.0
w, b = 0.0, 0.0
learning_rate = 0.1

p_before = sigmoid(w * x + b)
dw = (p_before - y) * x
db = p_before - y

# Both gradients are calculated before changing either parameter.
w_new = w - learning_rate * dw
b_new = b - learning_rate * db
p_after = sigmoid(w_new * x + b_new)
loss_before = -log(p_before)
loss_after = -log(p_after)

print(f"before: p={p_before:.4f}, loss={loss_before:.4f}")
print(f"after: w={w_new:.2f}, b={b_new:.2f}")
print(f"after: p={p_after:.4f}, loss={loss_after:.4f}")

assert abs(w_new - 0.1) < 1e-12
assert abs(b_new - 0.05) < 1e-12
assert abs(p_after - 0.5621765) < 1e-6
assert loss_after < loss_before
