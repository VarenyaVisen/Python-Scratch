# Logical operators = evaluate multiple conditions(or, and, not)
#                     or = at least one condition is True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# OR
temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scehduled")


# AND
temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0  and is_sunny == False:
    print("It is cold outside")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
else:
    print("The weather is awesome")

# NOT
is_student = False

if not is_student:
    print("you're not a student")