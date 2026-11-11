"""Lesson 3: trace gradient descent on f(x)=(x-3)^2."""

def f(x):
    return (x - 3.0) ** 2


def derivative(x):
    return 2.0 * (x - 3.0)


x = 1.0
learning_rate = 0.2
print("step | current x | f(x)")
for step in range(5):
    print(f"{step:4d} | {x:9.4f} | {f(x):.8f}")
    x = x - learning_rate * derivative(x)

# After updates at steps 0..4, the next point is x=2.84448.
assert abs(x - 2.84448) < 1e-10
