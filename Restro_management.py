def main():
    menu = {
        "PIZZA":110,
        "BURGER":50,
        "PASTA":120,
        "CHILLI PATATO": 140
    }
    print("Welcome to my Restaurent ,")
    print("Here is the menu of my restaurent ,")
    print("Pizza:110 \nBurger:50\nPasta:120\nChilli Patato: 140")

    order_total = 0
    item1 = input("You want to take something  ? (YES / NO) : ").upper()
    while item1 == "YES":
        order = input("Enter your order you want to eat : ").upper()
        if order in menu:
            order_total += menu[order]
            print(f"Your item {order} has been added to your order")
        else:
            print(f"Ordered item {order} is not available yet ! ")
        anything = input("Enter if you anything add in your order ? (YES / NO) : ").upper()
        if anything == "NO":
            break
            
    print(f"The total amount is {order_total}")
main()