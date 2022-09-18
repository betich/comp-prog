def get_sum(data):
    s = []  # [6538106021, [1, 2, 3. 4], 663292939321, [1, 2]]
    for i in range(0, len(data), 2):
        # data[i] => id
        # data[i+1] => score
        if data[i] in s:
            position = s.index(data[i])
            # เพิ่มคะแนนเข้าไปใน list => [id, [1, 3]]
            s[position+1].append(data[i+1])
            # s[position+1] += data[i+1]
        else:
            s.append(data[i])
            s.append([data[i+1]])

    for k in range(0, len(s), 2):
        # s[k] => id
        # s[k+1] => score[]
        if len(s[k+1]) > 3:
            min_value = min(s[k+1])
            s[k+1].remove(min_value)

        s[k+1] = sum(s[k+1])

        # sum_s = 0
        # for i in s[k+1]:
        #   sum_s += i
        # s[k+1] = sum_s

    return s


d = [
    6610013121, 4,
    6610021021, 5, 6610021021, 5,
    6610061121, 7, 6610061121, 5, 6610061121, 1,
    6610000121, 3, 6610000121, 2, 6610000121, 2, 6610000121, 3
]

out = get_sum(d)
print(out)
