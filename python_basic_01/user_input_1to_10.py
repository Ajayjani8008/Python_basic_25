user_input= int(input("Enter a number between 1 to 10 : "))

while user_input < 1 or user_input > 10:
    print("Invalid input Try again")
    user_input= int(input("Enter a number between 1 to 10 : "))

print("User input is ",user_input)