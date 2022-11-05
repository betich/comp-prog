a = []

for i in range(int(input())):
    c = [float(j) for j in str(input()).split()]
    a.append([i + 1, c[0], c[1], (c[0]**2 + c[1]**2)**0.5])

a = sorted(a, key=lambda x: x[3])
print('#', a[2][0], ': (', a[2][1], ', ', a[2][2], ')', sep='')
