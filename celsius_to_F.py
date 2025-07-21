temp = int(input("Enter the value of the temperature : "))
deg = input("Enter the temperature is in celsius ir fahrenhite : ").lower()
if deg == "celsius":
    fah = (temp * 9/5) + 32
    print(f"{temp} {deg} is in the Fahrenhite is {fah}")
elif deg == "fahrenhite":
    cel = (temp-32) * 5/9
    print(f"{temp} {deg} is in the Celsius is {cel}")
else:
    print("Invalid value of the temp")
