items =['apple', 'banana', 'apple', 'cherry', 'banana']

unique_items = set()

for item in items:
    if item not in unique_items:
        unique_items.add(item)
    else:
        print("Duplicate item found:", item)
        
print("Unique items:", unique_items)