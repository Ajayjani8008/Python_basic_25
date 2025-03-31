f = open("loops_tool_py/file1.py")

  
f.__next__() # read next line if not then send error message 
f.__next__()

for line in f:
    print(line,end="")
    
    
