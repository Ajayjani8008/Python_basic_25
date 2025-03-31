str = "aneem alahdnahd"

reversed_str = ""

reversed_str = "".join(str[i] for i in range(len(str) - 1, -1, -1))

print(reversed_str)


str_rev = ""
for char in (str):
    str_rev = char + str_rev
print(str_rev)