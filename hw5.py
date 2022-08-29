def next_partition_number(p, posnums):
    m = len(p)
    sum = 0
    i = 0
    sign = 1
    while m-posnums[i] >= 0:
        if i % 4 == 0 or i % 4 == 1:
            sign = 1
        if i % 4 == 2 or i % 4 == 3:
            sign = -1
        sum += p[m-posnums[i]]*sign
        i += 1
    return sum


def position_numbers(n):
    i = 1
    a = 1
    lst = [1]
    while i <= n:
        i += a
        lst.append(i)
        if i <= n:
            b = 2*a + 1
            i += b
            lst.append(i)
            a += 1
    return lst


def partition(n):
    n = int(n)
    posnums = position_numbers(n)
    p = [1]  # p[0] = 1
    for m in range(1, n+1):
        p += [next_partition_number(p, posnums)]
    out = str(p[n])

    return out


def find_id_in_num(id, num):
    id = str(id)

    m = 0
    for char in str(num):
        if char == id[m]:
            m += 1

    return m == len(id)


def least_pn_having(x):
    """
    รับ x เก็บจำนวนเต็มบวก
    คืน partition number ที่มีค่าน้อยสุดที่มีเลขทุกตัวใน x แฝงอยู่ตามลำดับที่ปรากฏใน x
    เช่น least_pn_having(12) คืน 1002
        least_pn_having(1234567890) คืน 1980769965254371045106648307068906619
    """

    m = 0
    while True:
        p = partition(m)
        if find_id_in_num(x, p):
            print(m, "=>", p)
            break
        else:
            m += 1

    return partition(m)


print(least_pn_having(6430342121))
