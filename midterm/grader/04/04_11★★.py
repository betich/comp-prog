user_input = str(input())
x = []

a = user_input[0]
for i in range(len(user_input)):
    b = user_input[i]
    if b == a:
        if i == 0:
            x.append([b, 1])
        else:
            x[-1][1] += 1
    else:
        x.append([b, 1])
    a = user_input[i]

for m in x:
    print(m[0], m[1], end=' ')
print()
