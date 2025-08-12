# typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Type casting float to int
gpa = int(gpa)
print(gpa)
print(type(gpa))

# int to float
age = float(age)
print(age)
print(type(age))

# float to string
age = str(age)
print(age)
print(type(age))

# str to bool
name = bool(name)
print(name)
print(type(name)) # empty = false

# Note = You cannot concatenate different data types 