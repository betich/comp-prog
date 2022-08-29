import math

[x, y, z] = [int(input()) for x in range(3)]


def quadratic_formula(a, b, c):
    return [(-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)]


[ans1, ans2] = quadratic_formula(x, y, z)

print(round(ans1, 3), round(ans2, 3))
