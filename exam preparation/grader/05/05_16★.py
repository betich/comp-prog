n = int(input())
x = [str(n)]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    x.append(str(n))

print("->".join(x[-15:]))
