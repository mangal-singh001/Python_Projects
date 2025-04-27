# import random
# print("Welcome to the Snake-Water-Gun game. You will be play this game with computer")
# def game(players):
#     if players == "SNAKE" or players == "WATER" or players == "GUN": 
#         comp = random.choice(["SNAKE","WATER","GUN"])
#         print(f"Your's choice is {players} or Computer's choice is {comp}")
#         if players == "SNAKE" and comp == "WATER":
#             print("You won this game")
#             return "win"
#         elif players == "GUN" and comp == "SNAKE":
#             print("You won this game")
#             return "win"
#         elif players == "WATER" and comp == "GUN":
#             print("You won this game")
#             return "win"
#         elif players == comp:
#             print("Match is draw")
#             return "draw"
#         else:
#             print("You loss , Better luck next time ")
#             return "loss"
#     else:
#         print("Enter a valid value among SNAKE-WATER-GUN") 
    
    

# win,loss,draw= 0,0,0
# while True:
#     players = input("Choose the value among SNAKE-WATER-GUN to play this game  or Quit to quit this game : ").upper()
#     if players == "QUIT":
#         break
#     result = game(players)
#     if result == "win":
#         win+=1
#     elif result == "loss":
#         loss+=1
#     elif result == "draw":
#         draw+=1
            
# print("Thanks you to play this game ")
# print(f"Your's score is for win = {win}, loss = {loss}, draw = {draw}")    
        
        
        
        
        
        
        
        
# SCORE OF THIS GAME IS SAVE TO THE FILE AS A HIGH SCORE AND ANYONE MADE A NEW HIGH SCORE THAN IT WILL BE UPDATED THE NEW SCORE IN THE FILE AS A NEW HIGH SCORE 
        
        
        
        
        
import random
print("Welcome to the Snake-Water-Gun game. You will be play this game with computer")
def game(players):
    if players == "SNAKE" or players == "WATER" or players == "GUN": 
        comp = random.choice(["SNAKE","WATER","GUN"])
        print(f"Your's choice is {players} or Computer's choice is {comp}")
        if players == "SNAKE" and comp == "WATER":
            print("You won this game")
            return "win"
        elif players == "GUN" and comp == "SNAKE":
            print("You won this game")
            return "win"
        elif players == "WATER" and comp == "GUN":
            print("You won this game")
            return "win"
        elif players == comp:
            print("Match is draw")
            return "draw"
        else:
            print("You loss , Better luck next time ")
            
    else:
        print("Enter a valid value among SNAKE-WATER-GUN") 
    
    

win = 0
while True:
    players = input("Choose the value among SNAKE-WATER-GUN to play this game  or Quit to quit this game : ").upper()
    if players == "QUIT":
        break
    result = game(players)
    if result == "win":
        win+=1
    
            
print("Thanks you to play this game ")
print(f"Your's score = {win}")    

# in it the high score is stored in a file and anyone make a new high score then it will update the high score in the file 

high_score_file = "score4.txt"

try:
    with open("score4.txt","r") as file1:
        content = file1.read()
        if content.strip():
            high_score = int(content.strip())
        else: 
            high_score = 0
    
except FileNotFoundError:
    high_score = 0
    
print(f"High score = {high_score}")        
    
new_score = win
if new_score > high_score:
    with open("score4.txt","w") as file2:
        file2.write(str(new_score))
    
    with open("score4.txt","r") as file3:
        fd = file3.read()
        print(fd)
    
else:
    print("Better luck next time ")