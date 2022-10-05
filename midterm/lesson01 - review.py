# Midterm Review - ISE Comp Prog

# Lesson 01 - Basic I/O, Data types, Variables, Operators, Expressions, Statements

import math
print('hello')  # prints hello => displays hello as output

x = 50
print(x)  # prints 50


# Variable

name = "Thee"  # String
age = 18  # Int
weight = 42.5  # Float
height = 1.5e2  # Number (scientific notation)
is_poor = True  # Bool
x = 18 < 19  # Bool from statement
birth_date = [24, 12, 1989]  # List -> [day, month, year]


# Operations

a = 10
a = a + 5			# 15
a = a - 1			# 14
a = a * 2			# 28
a = a % 10		# 8
a = a ** 2		# 64
a = a // 10		# 6

a = 10
a += 5				# 15
a -= 1				# 14
a *= 2				# 28
a %= 10				# 8
a **= 2				# 64
a //= 10


# Type Conversions

s1 = "123.2"
s2 = " 456"
n = int(s1) + int(s2)         # 123 + 456 => 579
f = float(s1) + float(s2)     # 123.2 + 456.0 => 579.2
print(s1+s2 + ", " + str(n) + ", " + str(f))  # 123.2 456, 579, 579.2

print(int(1.9) + int(0.5))  # 1 + 0 = 1


# Accepting Numeric Input

a = int(input())  # converts input() into int
b = float(input())  # converts input() into float


# Math module

# import the math module for this code to work
# import math

degree = float(input())
radian = degree * 3.14159 / 180
radian = degree * math.pi / 180
radian = math.radians(degree)
s = math.sin(radian)
c = math.cos(radian)
g = math.log(1E100, 10)         # g = 100.0
print(s, c, g)


# Built-in functions

a = abs(-2)               # a = 2
b = round(2/3, 2)         # b = 0.67
c = max([4, 1, 5, 3])     # c = 5
d = min([4, 1, 5, 3])     # d = 1
e = sum([4, 1, 5, 3])     # e = 13
f = len([4, 1, 5, 3])     # f = 4
g = str(1234)             # g = "1234"
h = int("123")            # h = 123
i = float("-123.4")       # i = -123.4

print(a, b, c, d, e, f, g, h, i)
