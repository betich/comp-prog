n = 0
a = [int(i) for i in str(input()).split()]

for i in range(1, len(a) - 1):
    if (a[i - 1] < a[i]) and (a[i + 1] < a[i]):
        n += 1

print(n)
