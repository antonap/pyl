import math


def polysum(n, s):
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    length = (n * s) ** 2
    return round(area + length, 4)


print polysum(56, 86)
print polysum(22, 36)
print polysum(66, 66)
