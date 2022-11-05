# TODO Provide more advanced examples and explanations

# Repetition

# 'While' loop

# while (some condition)
# => loops until that condition is False

s = 0
k = 0

while k < 5:  # while k < 5 is True, (will stop looping when k < 5 is False)
    s += (2*k - 1) ** 2  # s = s + (2*k-1) **2
    k += 1  # increments k until k < 5

print(s)  # 85


# Example: Find the smallest number

# 1. Without Loop

# This following code reads five number from keyboard one by one without any loop. For each round, perform
# a comparison with the current min (min_v), and update the min_v if the input value is smaller.
# Print the smallest number out at the end of the code.

min_v = float(input()) 	# get the first value
v = float(input())			# get the second value
if v < min_v:						# find the min value between the first and second values
    min_v = v
v = float(input()) 	# get the third value
if v < min_v:				# find the min value between the current min and the third value
    min_v = v
v = float(input()) 	# get the fourth value
if v < min_v:				# find the min value between the current min and the fourth value
    min_v = v
v = float(input())  # get the fifth value
if v < min_v:				# find the min value between the current min and the fifth value
    min_v = v
print("min_v = ", min_v)


# 2. With Loop

# This code produces the same result as above but more concise using while loop.

min_v = float(input())
k = 0
while k < 4:
    v = float(input())
    if v < min_v:
        min_v = v
    k += 1
print(" min = ", min_v)


# Range

# range(n)    => [0, n) counts from 0 to n (stopping before n)
print(list(range(5)))   # [0, 1, 2, 3, 4]

# range(n1, n2)    => [n1, n2) ()
print(list(range(1, 5)))    # [1, 2, 3, 4]

# range(n1, n2, step)   => [n1, n2) incrementing in steps
range(list[range(1, 5, 2)])   # [1, 3] (increment by 2)


# 'For' Loop

# It's basically just counting aaaa

# for example: the below code
for i in range(5):  # range counts from 0 to n [0, n) (stopping before n)
    print(i)

# is equivalent to this code
print(0)
print(1)
print(2)
print(3)
print(4)


# or
for i in ["a", "b", "c"]:
    print(i)


# is equivalent to
print("a")
print("b")
print("c")


# Example: Dot Product between u and v

# This code gets u as a string of numbers separated by space from keyboard:
# Example input:
# u : 1 2 0 2 1
# v : 2 2 1 2 2
# Then, calculate the dot product between u and v and print out the result.

x = input().split()
u = [0.0]*len(x)
for i in range(len(x)):
    u[i] = float(x[i])

x = input().split()
v = [0.0]*len(x)
for i in range(len(x)):
    v[i] = float(x[i])

dot = 0
for i in range(len(x)):
    dot += u[i]*v[i]

print(dot)


# Example: Check if the answer is correct

# This code gets u as a string of numbers separated by space from keyboard:
# Example input:
# u : 1 2 0 2 1
# v : 2 2 1 2 2
# Then, calculate the dot product between u and v and print out the result.

x = input().split()
u = [0.0]*len(x)
for i in range(len(x)):
    u[i] = float(x[i])

x = input().split()
v = [0.0]*len(x)
for i in range(len(x)):
    v[i] = float(x[i])

dot = 0
for i in range(len(x)):
    dot += u[i]*v[i]

print(dot)


# Example: Count the number of digits in a string

# This code counts the number of digits appear in a string.
# Example of input: Hello2123BD
# Expected output will be 4, counted by 2, 1, 2, 3

# Approach 1
s = input()
digit_counts = 0
for ch in s:
    if "0" <= ch <= "9":
        digit_counts += 1
print(digit_counts)


# Approach 2

s = input()
digit_counts = 0
for ch in s:
    if ch.isdigit():
        digit_counts += 1
print(digit_counts)
