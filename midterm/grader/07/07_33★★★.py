dir1, dir2 = str(input()).split()
a = [x.strip().split() for x in open(dir1)] + [x.strip().split()
                                               for x in open(dir2)]
a = sorted(sorted(a, key=lambda x: int(x[0])), key=lambda x: int(x[0][-2:]))
for x in a:
    print(x[0], x[1])
