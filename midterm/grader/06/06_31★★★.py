mo = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
zs = ["Aquarius", "Pisces", 'Aries', 'Taurus', 'Gemini', 'Cancer',
      "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", ]


def read_date():
    date = input().split()
    return [int(date[0]), mo.index(date[1]) + 1, int(date[2])]


def zodiac(d, m):
    if d > 21:
        return zs[m-1]
    return zs[(m - 2) % 12]


def days_in_feb(y):
    if not y % 400 or y % 100 and not y % 4:
        return 29
    return 28


def days_in_month(m, y):
    if m == 2:
        return days_in_feb(y)
    dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dm[m - 1]


def days_in_between(d1, m1, y1, d2, m2, y2):
    t1 = (337 + days_in_feb(y1)) - \
        (sum([days_in_month(x, y1) for x in range(1, m1)]) + d1)
    t2 = sum([sum([days_in_month(m, y) for m in range(1, 13)])
             for y in range(y1+1, y2)])
    t3 = sum([days_in_month(x, y2) for x in range(1, m2)]) + d2
    return t1 + t2 + t3 - 1


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))


exec(input().strip())
