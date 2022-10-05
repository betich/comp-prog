a, b = input().split()

scores = [float(x.replace('\n', '')[-5:])
          for x in open(a, 'rt') if x.replace('\n', '')[:2] == b[2:]]
if scores == []:
    print('No data')
else:
    print(min(scores), max(scores), sum(scores) / len(scores))
