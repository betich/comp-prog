key = [*input()]
ans = [*input()]
score = 0
if len(key) != len(ans):
    print('Incomplete answer')
else:
    for i in range(0, len(key)):
        if key[i] == ans[i]:
            score += 1
    print(score)
