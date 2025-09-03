name = input("Enter your full name: ").lower()

#len() it gives the length of the string
result = len(name)

print(f"The length of the name is : {result}")

# find method will give us the first occurrence of a given character
result2 = name.find("a")
print(f"The first occurrence of letter a is at : {result2}")

# to find the last occurrence we use rfind()
result3 = name.rfind("a")
print(f"The last occurrence of letter a is at : {result3}")

# name.capetalize() : this method is used to capetalize the fist letter of the string 
# name.upper() : it makes all the characters in uppercase
# name.lower() : it makes all the characters in lowercase
# name.isdigit() : returns boolean value if string is only numbers
# name.isalpha() : it will return True or False based on if a string contians only alphabetical characters
# name.count("-") : it is used to determine the number of occurrences of a specified value within a sequence
# name.replace("-", " ") : it replaces the first input with the second one its one of the most important and used method

print(help(str))