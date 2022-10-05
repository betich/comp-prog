# Functional programming

# Why use functions?
# 1. Reuse code
# 2. Organize code
# 3. Reduce complexity

# For example

print("Good morning teethanarit, have a nice day")
print("Good morning ttthhheeeeeeeee, have a nice day")
print("Good morning teetri, have a nice day")
print("Good morning betich, have a nice day")

# This code is repetitive

# We can use function to make code more readable


def good_morning(name):
    print("Good morning " + name + ", have a nice day")


good_morning("teethanarit")
good_morning("ttthhheeeeeeeee")
good_morning("teetri")
good_morning("betich")

# How to use function

# Create a function


def say_hello():
    print("Hello from a function")

# To call the function


say_hello()  # Hello from a function

# Function with arguments


def hello_person(name):
    print("Hello " + name)


hello_person("Tee")  # Hello Tee

# Function with return value


def add(a, b):
    return a + b


c = add(1, 2)
print(c)  # 3

# Variable scope

a = 1  # Global variable


def my_function():
    a = 2  # Local variable
    # Local variable will override global variable
    # But local variable will be destroyed after the function is called
    print(a)  # 2


print(a)  # 1

# Example: Calculate the dot product between u and v


def dot_product(u, v):
    dot = 0
    for i in range(len(u)):
        dot += u[i]*v[i]
    return dot


u = [1, 2, 0]
v = [2, 2, 1]
answer = dot_product(u, v)
print(answer)  # 6

# Example: find intersection of two lists


def intersection(list1, list2):
    result = []
    for x in list1:
        if x in list2:
            result.append(x)
    return result


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(intersection(a, b))  # [3, 4, 5]
