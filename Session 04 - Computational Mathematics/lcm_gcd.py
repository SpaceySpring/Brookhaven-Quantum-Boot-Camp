import numpy as np

x = np.gcd(447618, 2011835)
y = abs(447618 * 2011835)
lcm = y / x
print(f"the least common denominator is {lcm}")
