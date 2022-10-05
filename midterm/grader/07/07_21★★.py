import string

l = list(string.ascii_lowercase)
u = list(string.ascii_uppercase)


def rot13(x):
    if x in l:
        return l[(l.index(x) + 13) % 26]
    elif x in u:
        return u[(u.index(x) + 13) % 26]
    else:
        return x


a = []
while True:
    b = str(input())
    if b == 'end':
        break
    a.append(b)


a = [''.join(list(map(rot13, [*x]))) for x in a]

print('\n'.join(a))
