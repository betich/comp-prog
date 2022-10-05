[a, b, c, d] = [float(i) for i in input().split()]

if a > b:
    b, a = a, b
if b > c:
    c, b = b, c
if c > d:
    d, c = c, d
if a > b:
    b, a = a, b
if b > c:
    c, b = b, c
if a > b:
    b, a = a, b

print(round((b + c) / 2, 2))
