# Dictionary

# Dictionaries are used to store data values in key:value pairs.

# =================================

# Accessing data from a dictionry

# A dictionary is kinda like a list
# For a list, you use an index to get a value

import time
a = [1, 2, 3, 4]
print(a[1])  # 2

# For a dictionary, you use a key to get a value

a = {"one": 1, "two": 2, "three": 3, "four": 4}
print(a["one"])  # 1


grades = {"6130186221": "A", "6230221221": "A",
          "6231009821": "B", "6230543921": "C",
          "6230431521": "B", "6230276821": "A"}

print(grades["6130186221"])  # A

# You can also use a variable as a key

a = {"one": 1, "two": 2, "three": 3, "four": 4}
key = "one"
print(a[key])  # 1

# =================================

# Assigning data to a dictionary
a = {"one": 1, "two": 2, "three": 3, "four": 4}
a["five"] = 5

b = "six"
a[b] = 6

# =================================

# Keys and Values can be any type of data

my_dict = {"weather": "sunny", "temperature": 25, "wind": "calm",
           "humidity": 0.5, "id101": [1, 2, 3, 4], 101: 100, }


# But floating point keys are not encouraged

my_dict = {0.1: 'a', 0.2: 'b', 0.3: 'c', 0.4: 'd'}
k = 0.1
print(my_dict[k])  # a
k += 0.1  # 0.2
print(my_dict[k])  # b
k += 0.1  # 0.30000000000000001
print(my_dict[k])  # erro

# =================================

# Checking if k is in a dictionary
# Used for checking if a key is in a dictionary

a = {"one": 1, "two": 2, "three": 3, "four": 4}
print("one" in a)  # True
print("five" in a)  # False

# =================================

# Example: Checking if id is in dictionary


def read_data():
    x = input().split(", ")
    d = {"ID": x[0],
         "Name": x[1],
         "Birthdate": [int(x[2]), int(x[3]), int(x[4])]}
    return d


student1 = {"ID": "5830000021",
            "Name": "Pranpriya M.",
            "Birthdate": [27, 3, 1997]}
student2 = read_data()
print(student2)
# =================================


# Looping over a dictionary
# You can loop over a dictionary using a for loop

a = {"one": 1, "two": 2, "three": 3, "four": 4}
for key in a:
    print(key, a[key])

# OUTPUT
# one 1
# two 2
# three 3
# four 4

# =================================

# dict.keys(), dict.values(), dict.items()
# Returns a list of keys, values, or key:value pairs

a = {"one": 1, "two": 2, "three": 3, "four": 4}
print(a.keys())  # ['one', 'two', 'three', 'four']
print(a.values())  # [1, 2, 3, 4]
print(a.items())  # [('one', 1), ('two', 2), ('three', 3), ('four', 4)]


# You can also loop over a dictionary using the items() method

a = {"one": 1, "two": 2, "three": 3, "four": 4}
for key, value in a.items():   # destructing from a list
    print(key, value)

# =================================

# Bonus

# looping over a list of sorted keys

a = {"one": 1, "two": 2, "three": 3, "four": 4}

for key in sorted(a.keys()):
    print(key, a[key])


# sorting dictionary.items() by value

a = {"one": 1, "two": 2, "three": 3, "four": 4}
for v, k in sorted([(v, k) for k, v in a.items()]):
    print(v, k)

# =================================

# Bonus: Dictionary Comprehension

source = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
d = {k: v for k, v in source}

# =================================

# Example: Dict access time


def search_all(X):
    b = time.time()
    n = len(X)
    for i in range(n):
        if i in X:     # True
            pass
    for i in range(n):
        if (n+1) in X:  # False
            pass
    print(time.time() - b)


n = 10000
L = []
for i in range(n):
    L.append(i)
D = {}
for i in range(n):
    D[i] = i

search_all(L)
search_all(D)
