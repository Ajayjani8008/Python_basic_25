username = "jani"

def username_def():
    global username
    username= "ajay"
    print(username)


print(username)
username_def()

# print(username)


def clouser(num):
    def actual_clouser(x):
        return x ** num
    return actual_clouser

f= clouser(2)
g= clouser(3)

print(f(2))
print(g(2))
