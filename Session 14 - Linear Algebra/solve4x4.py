# solve4x4.py

import numpy as np


def lin_eq():
    equation = np.array([[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]])
    return equation


def equal_eq():
    solved = np.array([4, 16, 22, 15])
    return solved


def main():
    lin_eq()
    equal_eq()
    xa = np.copy(lin_eq())
    ya = np.copy(lin_eq())
    za = np.copy(lin_eq())
    wa = np.copy(lin_eq())

    # Overlay the value vector on a column in each unknown's matrix
    xa[:, 0] = equal_eq()
    ya[:, 1] = equal_eq()
    za[:, 2] = equal_eq()
    wa[:, 3] = equal_eq()

    # Calculate determinant of coefficients matrix
    det_lin_eq = np.linalg.det(lin_eq())

    # Use Cramer's rule to solve 3 x 3 system of linear equations
    x = np.linalg.det(xa) / det_lin_eq
    y = np.linalg.det(ya) / det_lin_eq
    z = np.linalg.det(za) / det_lin_eq
    w = np.linalg.det(wa) / det_lin_eq

    print(rf"x={x:,.0f}")
    print(rf"y={y:,.0f}")
    print(rf"z={z:,.0f}")
    print(rf"w={w:,.0f}")


main()
