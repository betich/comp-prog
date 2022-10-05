# String

s = "Hello"
t = ' Python'


# List

x = [1, 3, 5, 7]
y = [5, 6, 7, 8]
rps = ["rock", "paper", "scissors"]


# Concatenation

r = s + t   # Hello Python
z = x + y   # [1, 3, 5, 7, 5, 6, 7, 8]


# Length

print(len(s), len(t))  # 5, 7

# t = ' Python'
# t = 'xxxxxxx'=> len(t) is 7


# Accessing Values

x = [1, 3, 5, 7]
# [0, 1, 2, 3]
# [-4, -3, -2, -1]

print(x[0], x[2])    # 1 5
print(x[-1], x[-2])  # 7 5


# Slicing

s = "Hello there, General Kenobi."
print(s[0:3:1])  # startindex, stopindex(NOT include), step

print(s[5:11:1])  # there
print(s[0:11:2])  # Hlotee

print(s[-1:-4:-1])  # .1b

x = ["A", "B", "C", "D"]
print(x[1:4:1])   # ['B', 'C', 'D']

print(x[-3:3:1])  # ['B', 'C']


# Repetition (Multiplication)
a = 10*[0]
b = [23]*5
s1 = "Ora"*10
s2 = 10*"Muda"

print(a)    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(b)    # [23, 23, 23, 23, 23]
print(s1)   # OraOraOraOraOraOraOraOraOraOra
print(s2)   # MudaMudaMudaMudaMudaMudaMudaMudaMudaMuda


# Example

# 1. Get info from student ID

s = input()   # 6230002321
enYear = s[:2]     # 62
degree = s[2]    # 3
faCode = s[-2::1]    # 21

# 2. Get a number from keyboard and print its corresponding day.

days = ["MO", "TU", "WE", "THU", "FRI", "SAT", "SUN"]
k = int(input())    # 5
k -= 1
print(days[k])    # FRI

# Other String Functions

s = "    I have a bad feeling about this.    "
s1 = s.upper()
s2 = s.lower()
s3 = s.strip()

print(s1)    # "    I HAVE A BAD FEELING ABOUT THIS.    "
print(s2)    # "    i have a bad feeling about this.    "
print(s3)    # "I have a bad feeling about this."
print(s)   # "    I have a bad feeling about this.    "
