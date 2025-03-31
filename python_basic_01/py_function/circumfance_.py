import math

def circle_circumference(radius):
    return round(2 * math.pi * radius,2)


print(circle_circumference(5))

def circle_area(radius):
    return format(math.pi * radius**2,'.2f')

print(circle_area(5))

def pythagoras(a,b):
    return f"{math.sqrt(a**2 + b**2):.2f}"

print(pythagoras(3,4))