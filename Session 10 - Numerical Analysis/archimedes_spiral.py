import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def cal_arc(theta):
    return np.sqrt(1 + (theta**2))


mn = 0
mx = 8 * np.pi
steps = 1000
t = np.linspace(mn, mx, steps)
r = t
x = r * np.cos(t)
y = r * np.sin(t)

s = quad(cal_arc, mn, mx)
print(s)

# plt.subplot(projection="polar")
plt.title("Archimedes Spiral")
plt.xlabel("x = r * np.cos(t)")
plt.ylabel("y = r * np.sin(t) ")
plt.plot(x, y)
plt.axhline(0, color="grey")
plt.axvline(0, color="grey")
plt.grid()
plt.show()
