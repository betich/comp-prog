g = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A']
a = []
b = []
while True:
    x = str(input()).split()
    if x == ['q']:
        break
    a.append(x[0])
    b.append(x[1])
c = str(input()).split()
for i in c:
    b[a.index(i)] = g[g.index(b[a.index(i)]) + 1]

for i, j in zip(a, b):
    print(i, j)
