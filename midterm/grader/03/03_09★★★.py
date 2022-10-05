from math import sin, pi

x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

[d1, m1, y1, d2, m2, y2] = [int(i) for i in input().split()]
y1, y2 = y1 - 543, y2 - 543

# red
if (y1 % 400 == 0) or (y1 % 4 == 0 and y1 % 100 != 0):
    x[1] = 29
red = sum(x[m1:]) + x[m1 - 1] - d1 + 1
x[1] = 28

# black
black = 365 * (y2 - y1 - 1)

# blue
if (y2 % 400 == 0) or (y2 % 4 == 0 and y2 % 100 != 0):
    x[1] = 29
blue = sum(x[:m2 - 1]) + d2 - 1
x[1] = 28

total = red + black + blue

# calculate
phy = sin(2 * pi * total / 23)
emo = sin(2 * pi * total / 28)
intel = sin(2 * pi * total / 33)

print(total, "{:.2f}".format(phy),
      "{:.2f}".format(emo), "{:.2f}".format(intel))
