input_str= "teeteralmaflgpqbva;"

for char in input_str:
    print(char)
    if (input_str.count(char)) == 1:
        print("charector is",char)
        break