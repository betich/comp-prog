import re

a = str(input())
a = re.split(r'[^A-Za-z0-9]+', a)
a = [x for x in a if x]
a = [a[0].lower()] + [x.capitalize() for x in a[1:]]
a = ''.join(a)
print(a)
