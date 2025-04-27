import random
print("Welcome to the Rock-Paper-Scissors game : ")

def game(players):
    if players == "ROCK" or players == "PAPER" or players == "SCISSOR":
        computer = random.choice  (["ROCK","PAPER","SCISSOR"])
        print(f"Your's choice is {players} and Computer's choice is {computer}")
        if players == computer:
            print("Match is draw, Please play again")
        elif players == "SCISSOR" and computer == "PAPER":
            print("You won, You palyed really well")
        elif players == "PAPER" and computer == "ROCK":
            print("You won, You palyed really well")
        elif players == "ROCK" and computer == "SCISSOR":
            print("You won, You palyed really well")
        else:
            print("You loss, Better luck next time")
    else:
        print("Enter a valid value among ROCK-PAPER-SCISSOR")
    
    
players = input("Enter your choice among Rock-Paper-scissor to play this game with computer : ").upper()
game(players)



