# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condidtion else Y


num = 5
a = 6
b = 7
user_role = "admin"

print("Positive" if num > 0 else "Negative")

result = "Even" if num%2 == 0 else "Odd"
print(result)

max_num = a if a>b else b
min_num = a if a<b else b

print(f"Max number : {max_num}")
print(f"Min number : {min_num}")

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"You have : {access_level}")


