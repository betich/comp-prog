d = [int(i) for i in input().split()]
p = d[-1]
i = -1
j = 0
n = len(d)

while True:

    if d[j] <= p:
        i += 1
        d[i], d[j] = d[j], d[i]
    j += 1

    if not (j < n):
        break

print(d)
