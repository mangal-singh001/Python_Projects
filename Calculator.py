a= int(input("Enter the value 1:"))
b= int(input("Enter the value 2:"))
opr= input("Enter Opr:")
c = a+b
d = a-b 
e = a*b
f = a/b

if opr == "+":
    print(c)
elif opr == "-":
    print(d)
elif opr == "*":
    print(e)
elif opr == "/":
    print(f)
else:
    print("invalid operand")
    

