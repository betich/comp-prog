def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    N += 1
    while not is_prime(N):
        N += 1
    return N


def next_twin_prime(N):
    while True:
        a = next_prime(N)
        b = next_prime(a)
        if b - a == 2:
            return (a, b)
        N += 1


exec(input().strip())

'''
def main():
    n = int(input())
    print(next_twin_prime(n))


if __name__ == "__main__":
    main()
'''
