import numpy as np

# limit
n = 1899

# range of natural numbers to the limit
xn = np.arange(1, n + 1)

# choosing the terms that are divided by 7 and 11
x = xn[(xn % 7 == 0) & (xn % 11 == 0)]
print(x)

# summing
y1 = np.cumsum(x)
print(y1)
print(f"The sum of tall the natural numbers that divide into 7 and 11 is {y1[-1]}")
