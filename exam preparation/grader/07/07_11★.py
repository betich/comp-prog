a = str(input())
if a[-1] in ['x', 's']:
    a += 'es'
elif a[-2:] == 'ch':
    a += 'es'
elif a[-1] == 'y' and a[-2] not in ['a', 'e', 'i', 'o', 'u']:
    a = a[:-1] + 'ies'
else:
    a += 's'
print(a)
