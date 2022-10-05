import re

count = 0
word = str(input())
sentence = re.split(r'\W', str(input()))
for i in sentence:
    if i == word:
        count += 1
print(count)
