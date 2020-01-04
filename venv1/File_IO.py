# We can read and write from a file by first opening it using the open function.
employee_file = open('Employees.txt','r')
# Readable() function: this function is supposed to return true or false based on whether it can read a file.
# For some reason, print(employee_file.readable()) does not work in my PyCharm. Maybe because
# I am using Python 2 interpreter.
# print(employee_file.readable())

print("---x---x---x---")
# Readline() function: It reads each individual line one by one.
print(employee_file.readline()) # If I call this function again, it will print the next line.

# you can also get each element from the array such as:
print(employee_file.readlines()[0])

# Readlines() function: this will take all the lines from the file and put it in an array.
print(employee_file.readlines())

# Read() function: This function reads the entire file in one go and prints out the file as an exact
# copy of the text/ reading file.
print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()