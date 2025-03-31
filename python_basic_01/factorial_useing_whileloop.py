number = int(input("Enter a number : "))
if number < 0:
    print("Factorial is not possible")
    number = int(input("Enter a new number : "))
elif number > 1000:
    print("Factorial is too large")
    number = int(input("Enter a new number : "))
    
factorial = 1


while number > 0:
    factorial = factorial * number 
    number = number - 1

print(factorial)
