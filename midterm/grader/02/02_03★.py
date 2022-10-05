m = ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"]

a = str(input())
b = list(map(int, a.split('/')))

print(m[b[1] - 1], ' ', b[0], ', ', b[2], sep='')
