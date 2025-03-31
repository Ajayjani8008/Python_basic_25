def print_kargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kargs (name="jani",age=22)
print_kargs (name="ajay",age=22,address="bhavnagar")