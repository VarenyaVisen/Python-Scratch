# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print(f"You are eligible for the credit card")

elif age < 0 :
    print("Invalid age!!!")

else:
    print("Sorry you're not eligible")



response = input("Enter your response : ").lower()
if response == "y":
    print("You will get the food")

else:
    print("You will not get the food")