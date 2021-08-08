"""
Challenge #377 [Easy] Axis-aligned Crate Packing
"""

def fit1(X, Y, x, y):
    return (X // x) * (Y // y)


def fit2(X, Y, x, y):
    orientations = (fit1(X, Y, x, y),
                    (X // y) * (Y // x))

    return max(orientations)


def fit3(X, Y, Z, x, y, z):
    orientations = ((X // x) * (Y // y) * (Z // z),
                    (X // x) * (Y // z) * (Z // y),
                    (X // y) * (Y // x) * (Z // z),
                    (X // y) * (Y // z) * (Z // x),
                    (X // z) * (Y // x) * (Z // y),
                    (X // z) * (Y // y) * (Z // x))

    return max(orientations)

#  Missing fitN for the moment

print('Fit 1:')
print(fit1(25, 18, 6, 5))
print(fit1(5, 100, 6, 1))
print(fit1(12345, 678910, 1112, 1314))
print('\nFit 2:')
print(fit2(25, 18, 6, 5))
print(fit2(5, 100, 6, 1))
print(fit2(12345, 678910, 1112, 1314))
print('\nFit 3:')
print(fit3(12, 34, 56, 7, 8, 9))
print(fit3(123, 456, 789, 10, 11, 12))
print(fit3(1234567, 89101112, 13141516, 171819, 202122, 232425))
