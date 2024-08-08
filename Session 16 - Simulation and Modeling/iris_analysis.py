# iris_analysis.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

"Chat GPT helped"


# Function to read CSV file and handle mixed data types
def read_csv(file_path):
    with open(file_path, "r") as f:
        # Skip the header
        next(f)
        # Read and parse the remaining lines
        data = [line.strip().split(",") for line in f]

    # Separate the columns
    sl = np.array([float(row[0]) for row in data])
    sw = np.array([float(row[1]) for row in data])
    pl = np.array([float(row[2]) for row in data])
    pw = np.array([float(row[3]) for row in data])
    var = np.array([row[4].strip('"') for row in data])  # Strip extra quotes

    return sl, sw, pl, pw, var


# Read experiment data from data file
file_name = "iris.csv"
file_path = Path(__file__).parent / file_name
sl, sw, pl, pw, var = read_csv(file_path)

# Plot the data
plt.figure()
colors = {"Setosa": "red", "Versicolor": "blue", "Virginica": "green"}

# Scatter plot with proper labeling
for variety in np.unique(var):
    indices = np.where(var == variety)
    plt.scatter(pl[indices], pw[indices], color=colors[variety], label=variety)

# Adding plot labels and title
plt.title("Iris Analysis")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.grid(True)
plt.legend(loc="best")
plt.show()
