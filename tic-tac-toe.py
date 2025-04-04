import tkinter as tk  # tkinter is a Python module for creating GUI applications 
from tkinter import messagebox  # messagebox provides pop-up message boxes (for showing the winner or draw message)


# this function checks if a player has won or if the match is a draw
def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green") # the winning buttons turn green for better visibility 
          
            messagebox.showinfo("Tic-Tac-Toe",f"Player {buttons[combo[0]]['text']} wins!")  # show the winner 
            root.quit()    # disabling buttons
            
            
    # checking for a draw 
    # the all() function checks if every button is filled (text is not empty)
    
    # if all buttons are filled and there is no winner, the game ends in a draw
    
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw !")
        
        
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()
        
# This swaps the current player
# this label at the bottom updates with the next players turn 
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")
    
    
    
# create a Tkinter window(root)
# sets the window title to "Tic-Tac-Toe"
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root,text="",font=("normal",25),width=6,height=2, command=lambda i=i: button_click(i)) for i in range(9)]  # this creates 9 buttons in a list 

# placing buttons in 3*3 grid
for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)
    
current_player = "X"
winner = False

# display a label at the bottom to show whose turn it is 
label = tk.Label(root,text=f"player {current_player}'s turn",font = ("normal",16))
label.grid(row=3, column=0, columnspan = 3)
# Starts the GUI loop, allowing the game to run and accept clicks 
root.mainloop()