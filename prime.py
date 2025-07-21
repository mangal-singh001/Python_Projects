a =  int(input("Enter the number to check it is prime or not : "))

if a <= 1:
    print("number is not prime")
else:
    prime = True # it is used to initialize a variable we assume in the beginning that the number is prime 
    for i in range(2,a):
        if a%i == 0: # == 0 is used to check the remainder of the number 
            prime = False
            break 
        
if prime: # prime is used to determine the final output
    print("number is prime")
else:
    print("Number is not prime")