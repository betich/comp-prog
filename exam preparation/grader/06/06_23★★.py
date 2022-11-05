def make_int_list(x):
    return [int(a) for a in x.split()]


def is_odd(e):
    return e % 2 != 0


def odd_list(alist):
    return list(filter(lambda x: x % 2 != 0, alist))


def sum_square(alist):
    return sum([a ** 2 for a in alist])


exec(input().strip())

'''
def main():
    print(make_int_list('12 3 45'))
    print(is_odd(3333))
    print(odd_list([1, 2, 3, 4, 5, 6, 7]))
    print(sum_square([1, 1, 2, 3]))


main()
'''
