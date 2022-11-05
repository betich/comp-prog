# List Comprehension


data = [1, 1, 4]  # [2, 3, 7]

print([data[i] + i + 1 for i in range(len(data))])

# Advanced Read File

f1 = open("score01.txt")

# print(lines)

a = []
for line in f1:
    a.append(line.strip().split())

# [["62100000", "54"], ["62100010", "56"]]
a1 = [[int(e) for e in line.strip().split()]
      for line in f1 if line[:2] == "62"]

# b = []
# for i in range(len(a)):
#   b.append(int(a[i][1]))
# print(round(sum(b)/len(a),1))


print(a1)
