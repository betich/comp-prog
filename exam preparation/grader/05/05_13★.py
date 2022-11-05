x = []
y = []

for i in range(int(input())):
    y.append(int(input()))

y = y + [int(i) for i in str(input()).split()]

while True:
    try:
        if y[-1] == -1:
            break
    except:
        pass
    y.append(int(input()))


for i in range(len(y) - 1):
    if i % 2 == 0:
        x.append(y[i])
    else:
        x.insert(0, y[i])

print(x)
