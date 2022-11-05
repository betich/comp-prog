a = list(str(input()))
for i in range(len(a)):
    if a[i] == '(':
        a[i] = '['
    elif a[i] == ')':
        a[i] = ']'
    elif a[i] == '[':
        a[i] = '('
    elif a[i] == ']':
        a[i] = ')'

print(''.join(a))
