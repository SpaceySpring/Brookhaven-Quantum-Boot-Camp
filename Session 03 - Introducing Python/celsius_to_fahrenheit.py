import numpy as np

# Make a range of numbers starting from -44 to 104 Celsius in steps of 4
C = np.arange(-44, 105, 4)
for i in C:
    # change celsius to fahrenheit
    F = (i * 9 / 5) + 32
    print(f"{i:.2f}C is {F:.2f}F")

# Verify -40, 0, 100
C = [-40, 0, 100]
for i in C:
    # change celsius to fahrenheit
    F = (i * 9 / 5) + 32
    print(f"{i:.2f}C is {F:.2f}F")
