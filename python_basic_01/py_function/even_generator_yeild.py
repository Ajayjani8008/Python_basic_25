def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i       
        
number= even_generator(10)

for i in number:
    print(i)
            
            
            