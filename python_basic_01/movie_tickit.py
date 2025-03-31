age = int(input("Enter your age : "))

day = int(input("Enter the day : "))

price = 12 if age >= 18 else 7

if day == 1:
    price = price * 0.9
elif age >= 18:
    price = price * 0.8
elif age == 18:
    price = price * 0.5
else:
    print("You can't see movie")

print("Ticket price is : ",price)