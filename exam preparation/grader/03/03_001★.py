[a, b, c, d, e] = [int(input()) for _ in range(5)]

# print(a, b, c, d, e)

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
if a > c:
    b, d, c = d, b, a

a = e

if a > b:
    a, b = b, a
if c > a:
    b, d, a = d, b, c

if a > d:
    print(d)
else:
    print(a)
