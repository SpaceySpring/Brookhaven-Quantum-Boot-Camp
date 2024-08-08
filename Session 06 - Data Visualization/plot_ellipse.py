# plot_circle.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

a = 100
b = 50
t = np.linspace(0, 2 * np.pi, 1000)
r = 1 / np.sqrt((np.cos(t) / a) ** 2 + (np.sin(t) / b) ** 2)
x = r * np.cos(t)
y = r * np.sin(t)
ellipsis = (x / a) ** 2 + (y / b) ** 2

plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.title("Ellipsis: (x/100)**2+ (y/50)**2 = 1")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-110, 110)
plt.ylim(-60, 60)
plt.xticks(np.arange(-100, 100.1, 100 / 5))
plt.yticks(np.arange(-50, 50.1, 100 / 10))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.scatter(0, 0)
plt.grid("on")
plt.gca().set_aspect("equal")
plt.show()

#rf is to look at the raw data (no back slashes) When printing 