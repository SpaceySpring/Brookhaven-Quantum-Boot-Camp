import numpy as np

n = 1000
x = np.arange(1, n + 1)
x_2 = x**2

x_2_sum = np.cumsum(x_2)
print(x_2_sum)

y2 = ((2 * (x) ** 3) + (3 * (x) ** 2) + x) / 6
print(y2)

print(np.array_equal(x_2_sum, y2))
