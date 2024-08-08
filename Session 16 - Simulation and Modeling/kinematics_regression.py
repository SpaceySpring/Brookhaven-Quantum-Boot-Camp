# kinematics_regression.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fit_quadratic(x, y):
    # Reshape vector x to become matrix x
    x = x[:, np.newaxis]
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    # The matrix x2 will have two columns:
    # 1) the original x values and 2) the x**2 values
    x2 = np.array(transformer.transform(x))
    model = LinearRegression().fit(x2, y)
    print(model.coef_)
    a = model.coef_[1]
    b = model.coef_[0]
    c = model.intercept_
    return a, b, c


def main():
    # Read experiment data from data file
    file_name = "kinematics_regression.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(file_path, delimiter=",")

    # time in seconds, distance in meters
    t, d = data.T

    # Calculate line of best fit
    a, b, c = fit_quadratic(t, d)

    # Calculate and print initial velocity (v) and acceleration (a)
    v = a
    acc = b
    print(f"Velocity = {v:.2f} m/s")
    print(f"Acceleration = {acc:.2f} m^2/s^2")

    plt.figure(Path(__file__).name)
    plt.scatter(t, d)
    plt.plot(t, a * t**2 + b * t + c, label="Quadratic", c="r")
    plt.title(
        "Kinematics Regression\n"
        f"Velocity = {v:.2f}$m/s$ "
        f"Acceleration = {acc:,.2f}$m^2/s^2$"
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.grid("on")
    plt.show()


main()
