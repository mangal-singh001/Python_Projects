import random 
def main():
    number = random.randint(1,100)
    guess = None
    count = 0
    print("Welcome to the guess the number game and guess the number between 1 to 100 ")
    print("If you right guess the number , you will earn Points")
    
    while guess != number:
            try:
                guess = int(input("Guess the number : "))
                if 1 < guess > 100:
                    print("Guess the numbeer between 1 to 100")
                else:
                    count+=1
                    if  number > guess:
                        print("The Number is larger than guess")
                    elif number < guess:
                      print("The Number is smaller than guess")
                    elif number == guess:
                      print(f"Congratulations you guess the right number {number}")
               
            except ValueError :
                print("Please! Enter the integers value")

    print(f"You guess the number in {count} attempts")
if __name__ == "__main__":
    main()
    
