from math import gcd

[a, b, c] = str(input()).split(',')

#print(a, b, c)

x = int('0' + b + c) - int('0' + b)
# print(x)

y = int('0' + '9' * len(c) + '0' * len(b))
# print(y)

x += int('0' + a) * y

print(int(x // gcd(x, y)), '/', int(y // gcd(x, y)))
