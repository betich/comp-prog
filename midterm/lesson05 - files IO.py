
# Open a File

# Method 1 : readline()
# readline => return one line from the file

f1 = open("score.csv")    # opens the file

line1 = f1.readline()   # the first line
line2 = f1.readline()   # the second line
print(line1, line2)

# or use a loop

while True:
    line = f1.readline()
    if not line:
        break
    print(line)

f1.close()    # close the file


# Method 2 : readlines()
# readlines => returns every line in the file as an list

f2 = open("score.csv")

lines = f2.readlines()    # list of all the lines

for line in lines:
    print(line)


f2.close()    # close the file


# Method 3: for loop through file
# we can use a for loop directly through a file variable

f3 = open("score.csv")

for line in f3:   # loop through f3
    print(line)

f3.close()    # close the file


# Example: Sum through list


# Example Input
# ====
# student_id,Q1,Q2,Q3,Q4,Q5
# 5600148421,7,1,6,6,6
# 5600163621,0,1,2,6,8
# 5600186321,6,5,9,10,3
# 5600334721,5,1,2,7,7
# 5600486621,3,9,9,7,4
# 5600555421,5,1,6,7,7
# 5600574721,3,3,4,8,4
# 5600612321,8,10,8,6,5
# 5600622121,5,9,6,10,7

scores = [sum([int(e) for e in line.split(',')[1:]]) for line in lines[1:]]


# Write File

# Method 1: write()
# write => write a string to the file

f1 = open("score.csv", "w")    # opens the file

f1.write("student_id,Q1,Q2,Q3,Q4,Q5")    # write a string to the file

f1.close()    # close the file


# Method 2: writelines()
# writelines => write a list of strings to the file

f2 = open("score.csv", "w")    # opens the file

# write a list of strings to the file
f2.writelines(["student_id,Q1,Q2,Q3,Q4,Q5", "5600148421,7,1,6,6,6"])

f2.close()    # close the file
