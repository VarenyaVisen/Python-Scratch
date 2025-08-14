a, b = 10, 3
# Arithmetic Operators
print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus (Remainder) → 1
print(a ** b)  # Exponentiation → 1000

# Comparison Operators
print(a == b)  # Equal → False
print(a != b)  # Not equal → True
print(a > b)   # Greater than → True
print(a < b)   # Less than → False
print(a >= b)  # Greater or equal → True
print(a <= b)  # Less or equal → False

# Logical Operators
x, y = True, False

print(x and y)  # AND → False
print(x or y)   # OR → True
print(not x)    # NOT → False

# Assignment Operators
num = 5
num += 3   # num = num + 3 → 8
num -= 2   # num = num - 2 → 6
num *= 4   # num = num * 4 → 24
num /= 6   # num = num / 6 → 4.0
num %= 3   # num = num % 3 → 1.0
num **= 2  # num = num ** 2 → 1.0

# Bitwise Operators
p, q = 5, 3  # binary: 101, 011

print(p & q)  # AND → 1  (001)
print(p | q)  # OR → 7   (111)
print(p ^ q)  # XOR → 6  (110)
print(~p)     # NOT → -6
print(p << 1) # Left shift → 10 (1010)
print(p >> 1) # Right shift → 2 (10)

# Membership Operators
list1 = [1, 2, 3]
print(2 in list1)   # True
print(5 not in list1) # True

# Identity Operators
x = [1, 2]
y = [1, 2]
z = x

print(x is y)      # False (different objects in memory)
print(x is z)      # True  (same reference)
print(x is not y)  # True
