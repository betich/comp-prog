d = int(input())
m = int(input())
y = int(input()) - 543

x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    x[1] = 29
print((sum(x[:m - 1]) + d))
