x = str(input())
print(x)

a = int(x[3] + x[10] + x[17] + x[24] + x[31])
b = int(x[7] + x[12] + x[17] + x[22] + x[27])

print('a', a)
print('b', b)

c = a + b + 10000
d = str(c)[-4:-1]

print('c', c)
print('d', d)

e = str(int(d[0]) + int(d[1]) + int(d[2]))
print('e', e)
e = int(e[-1]) + 1

print('e', e)

letters = ["A", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
code = d + letters[e]

print(code)
