s = 0
n = 0
while True:
    a = input()
    if a == 'q':

        break
    s += float(a)
    n += 1

if n == 0:
    print('No Data')
else:
    print(round((s / n), 2))
