# import re

dna = [x.upper() for x in str(input()).strip()]
command = str(input()).strip()
if command == 'D':
    pattern = str(input()).strip()

for x in dna:
    if x not in ['A', 'T', 'G', 'C']:
        print('Invalid DNA')
        exit(0)

if command == 'R':
    convert = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    dna = [convert[x] for x in dna]
    dna.reverse()
    print(''.join(dna))
elif command == 'F':
    count = {
        'A': 0,
        'T': 0,
        'G': 0,
        'C': 0
    }
    for x in dna:
        count[x] += 1
    print('A=', count['A'], ', T=', count['T'],
          ', G=', count['G'], ', C=', count['C'], sep='')
elif command == 'D':
    # a = len(re.findall(re.compile(pattern), ''.join(dna)))
    # print(a)
    n = 0
    for i in range(len(dna) - len(pattern) + 1):
        check = True
        for j in range(len(pattern)):
            if not dna[i + j] == pattern[j]:
                check = False
        if check:
            n += 1
    print(n)
