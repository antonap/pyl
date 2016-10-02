
def clip(lo, x, hi):
    return max(lo, min(hi, x))
    print "_________________"
    print lo, x, hi
    xlo = max(lo, x)
    print "lo,x:", xlo
    xhi = min(hi, x)
    print "x,hi:", xhi

    return max(xlo, xhi)

print clip(-1.62, -6.63, 1.62)  # -1.62
print clip(-8.63, 4.86, 1.04)  # 1.04
print clip(-3.09, 3.51, 4.56)  # 3.51
print clip(-8.48, -7.47, -3.04)  # -7.47
print clip(-5.84, 6.58, -3.09)  # -3.09
print clip(6.0, 2.44, 9.84)  # 6.0
print clip(7.57, -6.47, 8.24)  # 7.57
print clip(-3.6, -4.98, -2.84)  # -3.6
print clip(-1.58, 1.43, -0.15)  # -1.05
