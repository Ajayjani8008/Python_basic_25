number = int(input("Enter a number : "))

is_prime = True
for i in range(2, int(number / 2)):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
