full = ['Robert', 'William', 'James', 'John', 'Margaret',
        'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy',
        'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

a = []
for i in range(int(input())):
    a.append(str(input()))
for j in a:
    if j in full:
        print(nick[full.index(j)])
    elif j in nick:
        print(full[nick.index(j)])
    else:
        print('Not found')
