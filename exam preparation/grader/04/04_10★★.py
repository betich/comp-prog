a = float(input())
b = a
l = 0
u = 0

while True:
    if b == 0:
        break
    b = b // 10
    u += 1

x = (l + u) / 2

while True:
    if abs(a - (10 ** x)) <= (10 ** (-10)) * max(u, 10 ** x):
        break
    if 10 ** x > a:
        u = x
    elif 10 ** x < a:
        l = x
    x = (l + u) / 2


print(round(x, 6))
