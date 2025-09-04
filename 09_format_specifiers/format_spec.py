# fprmat specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number)f = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3244654.14159
price2 = -987245.65
price3 = 126465.34

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.3f}")

print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

print(f"Price 1 is {price1:010}")
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:010}")

print(f"Price 1 is {price1:<10}")
print(f"Price 2 is {price2:<10}")
print(f"Price 3 is {price3:<10}")

print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:>10}")

print(f"Price 1 is {price1:^10}")
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")

print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:-}")
print(f"Price 3 is {price3:+}")

print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.3f}")