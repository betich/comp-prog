# boolean expression

# True, False
print('1 == 1:', 1 == 1)    # 1 == 1: True
print('1 == 0:', 1 == 0)    # 1 == 0: False
print('0 == "0":', 0 == "0")    # 0 == "0": False
print((0.1+0.1+0.1) == 0.3)   # False
print(0.1+0.1+0.1, 0.3)   # 0.30000000000000004 0.3
print(123456789123456789 == 123456789123456789)   # True


# Rational Operators (and or not)

# a and b
# not (a and b) -> not a or not b
# not (a or b) -> not a and not b
x = 3
a = x > 5   # False
b = x < 10  # True
y = a and b  # False
not_y = not a and not b  # False


# Conditions

x = 5


# if Statements

# if True => then do something
if x > 4:  # True
    print("x is more than 4")  # prints "x is more than 4"

if x > 6:  # Falwe
    print("this code won't run because x is not more than 6")


# else Statements

# if (if is False), then do this instead

x = 10
if x != 10:  # False
    print("x is not equal to 10")
else:  # if (if is False), then do this
    print("x is equal to 10")


# elif Statements

# if (if is False), then check for this condition

x = 14

if x % 5 == 0:  # False
    print("Fizz")
elif x % 7 == 0:  # if (if is False), then check for this
    print("Buzz")  # prints this
else:  # if everything is False, then do this (e=won't run if elif is True)
    print("Something")


# List comparison
# compares the list elements from left to right

# list comparison
a = [1, 2, 1]
b = [1, 3]
print('{} == {} : {}'.format(a, b, a == b))   # [1, 2, 1] == [1, 3] : False
print('{} > {} : {}'.format(a, b, a > b))   # [1, 2, 1] > [1, 3] : False
print('{} < {} : {}'.format(a, b, a < b))   # [1, 2, 1] < [1, 3] : True

birth_date = [2001, 10, 5]
print(birth_date > [1997, 9, 30])   # True


# String comparison
# compares each character from left to right
# + lowercase > UPPERCASE
# + alphabets have increasing value from `'A'` to `'Z'`
# + digits have increasing value from `'0'` to `'9'`
# + alphabet > digit

# String comparison
print("'a' < 'b' :", 'a' < 'b')   # 'a' < 'b' : True
print("'A' < 'Z' :", 'A' < 'Z')   # 'A' < 'Z' : True
print("'A' < 'a' :", 'A' < 'a')   # 'A' < 'a' : True
print("'a' < 'A' :", 'a' < 'A')   # 'a' < 'A' : False
print("'0' < 'A' :", '0' < 'A')   # '0' < 'A' : True
print("'0' < 'Z' :", '0' < 'Z')   # '0' < 'Z' : True

s = 'abz'
t = "abc"
print("'{}' == '{}' : {}".format(s, t, s == t))    # 'abz' == 'abc' : False
print("'{}' > '{}' : {}".format(s, t, s > t))    # 'abz' > 'abc' : True
print("'{}' < '{}' : {}".format(s, t, s < t))    # 'abz' < 'abc' : False


# Checking for data in string

# if t in string, if t not in string
s = 'abc123'
t = 'ac'
if t in s:
    print('found')
else:
    print('not found')


# Checking for data in list

# if e in list, if e not in list
d = [1, 3, 5, 7, '1']
x = 1
if x in d:
    print('found')
else:
    print('not found')
