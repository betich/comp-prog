def roundNum(a):
    if a >= 10:
        return round(a)
    else:
        return round(a, 1)


def main():
    n = int(input())

    if n < 10**3:
        print(n)
    elif n < 10**6:
        print(roundNum(n / 10**3), 'K', sep='')
    elif n < 10**9:
        print(roundNum(n / 10**6), 'M', sep='')
    else:
        print(roundNum(n / 10**9), 'B', sep='')


main()
