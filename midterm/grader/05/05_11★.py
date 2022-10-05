a = str(input())
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in a:
    if i in x:
        x.remove(i)

if len(x) == 0:
    print('None')
else:
    print(",".join(x))
