def distance1(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def distance2(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def distance3(c1, c2):
    d = ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
    return (d, d <= c1[2] + c2[2])


def perimeter(points):
    p = 0
    for a, b in zip(points, points[-1:] + points[:-1]):
        p += ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return p


exec(input().strip())

'''
def main():
    print(distance1(0, 0, 3, 4))
    print(distance2([0, 0], [3, 4]))
    print(distance3([1, 2, 0.3], [1.5, 3.2, 1.0]))
    print(perimeter([[0, 0], [0, 2], [2, 2], [2, 0]]))


main()
'''
