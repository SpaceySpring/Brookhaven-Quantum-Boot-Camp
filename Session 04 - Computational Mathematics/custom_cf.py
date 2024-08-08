import math

# The number of cf's that will print
MAX_TERMS = 7


# If the last number is a one then you would take that term out
# and add it to the second to last number
def normalize_cf(cf):
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1

        # Pop is to take it out
        cf.pop(-1)
    return cf


# Creates the max amount of cf's
def encode_cf(x):
    cf: list[int] = []
    while len(cf) < MAX_TERMS:
        cf.append(int(x))
        x = x - int(x)

        # This breaks when the cf is arriving close to zero
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


# Takes the cf to make it a real number
def decode_cf(cf):
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    return h_n / k_n


# This takes a real number and encodes it to a cf then back to
# a real number a real number
def eval_cf(x):
    cf = encode_cf(x)
    x2 = decode_cf(cf)
    print(f"{x} -> {cf} -> {x2}")


"""Above code is from Dr. Biersach"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""Below code is modified from Dr. Biersach"""


# The numbers that are evaluated
def main():
    xn = []
    for n in range(1, 10):
        # Formula to get evaluated numbers
        num = (1 + math.sqrt(4 * (n) ** 2 - 4 * (n) + 5)) / 2
        xn.append(num)
        eval_cf(num)
    print(xn)


main()
