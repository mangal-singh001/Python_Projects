rows = int(input("Enter number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows - i),end = "")
    print("*" * (2*i - 1))
    


rows = int(input("Enter number of rows : "))
for i in range(1,rows+1):
    print("*" * i)


# Diamond shape


rows = int(input("Enter number of rows for upper half : "))
for i in range(1,rows+1):
    print(" " * (rows - i),end="")
    print("*" * (2*i - 1))
    
for i in range(rows-1,0,-1):
    print(" " * (rows - i),end= "")
    print("*" * (2*i - 1))
    
    
    
    
# Hourglass shape 

rows = int(input("Enter number of rows for upper half : "))
for i in range(rows,0,-1):
    print(" " * (rows-i),end = "")
    print("*" * (2*i -1 ))
    
for i in range(2,rows+1):
    print(" " * (rows-i),end="")
    print("*" * (2*i - 1))


rows = 3
for i in range(1,rows+1):
    if i == 1 or i == rows:
        print("***") 
    else:
        print("* *")