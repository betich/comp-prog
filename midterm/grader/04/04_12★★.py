n = int(input())
a, b = [], []
for i in range(n):
    user_input = [int(j) for j in str(input()).split()]
    a.append(user_input[i % 2])
    b.append(user_input[i % 2 - 1])
mode = str(input())
if mode == "Zig-Zag":
    print(min(a), max(b))
elif mode == "Zag-Zig":
    print(min(b), max(a))
