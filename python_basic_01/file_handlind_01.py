
file = open('test.txt',"w")


try:
    file.write("Hello World")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()


with open("test.txt", "w") as file:
    file.write("Hello World")
    file.write("Hello World")

