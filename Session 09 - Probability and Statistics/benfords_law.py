from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

x = np.random.randint(1, 1_000_001, 100_000)
print(len(x))

# Makes a list of all the first number from each digit. Before broken off they are powered to the 100th
i_first = []
for i in x:
    j = i**100
    p_first = int(str(abs(j))[:1])  # This takes the digit's first number
    i_first.append(p_first)

# Makes a list of integers from 1 to 9
num = range(1, 10)

# Count the times 1 through 9 shows up in the list
cc = []
for j in num:
    count = 0
    for i in i_first:
        if i == j:
            count += 1
    cc.append(count)

# Calculates the probability of the the leading digits from the count and the size of the numbers
prob = []
for i in cc:
    prob_cal = (i / len(i_first)) * 100
    print(prob_cal)
    prob.append(prob_cal)

print(prob)
plt.figure(Path(__file__).name)
plt.bar(
    num,
    prob,
)
plt.title("Law of Anomalous Numbers (n={100000})")
plt.xticks(np.arange(0, 10, 1))
plt.yticks(np.arange(0, 27, 1))
plt.xlabel("Number")
plt.ylabel("Probability")
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))
plt.show()
