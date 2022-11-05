g = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A']
a = []
b = []
while True:
    x = str(input()).split()
    if x == ['q']:
        break
    a.append(x[0])
    b.append(x[1])

# new code

d = []
for i, j in zip(a, b):
    d.append([i, j])

d = sorted(d, key=lambda x: x[0])

a, b = [], []
for i in d:
    a.append(i[0])
    b.append(i[1])

# end

c = str(input()).split()

for i in c:
    b[a.index(i)] = g[g.index(b[a.index(i)]) + 1]

for i, j in zip(a, b):
    print(i, j)
