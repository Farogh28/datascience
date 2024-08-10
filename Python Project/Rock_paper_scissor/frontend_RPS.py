# import tkinter as tk

# app = tk.Tk()

# app.title("Rock Paper Scissor Game Layout")
# app.geometry("700x500")
# app.config(bg = "#022859")
# app.resizable(False, False)

# lbl = tk.Label(text="         Lets play Rock-Paper-Scissor         ", font = ("Arial", 30), anchor="center", background="lightblue")
# lbl.place(x = 0, y = 0 )







# app.mainloop()


# import tkinter as tk
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Rock Paper Scissors Game")
# root.geometry("400x400")

# # Dictionary to map numbers to choices
# choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

# # Function to reset the game
# def reset_game():
#     b1["state"] = "active"
#     b2["state"] = "active"
#     b3["state"] = "active"
#     l1.config(text="Player")
#     l3.config(text="Computer")
#     l4.config(text="")

# # Function to disable buttons
# def button_disable():
#     b1["state"] = "disable"
#     b2["state"] = "disable"
#     b3["state"] = "disable"

# # Function to determine the winner
# def determine_winner(player_choice):
#     computer_choice = choices[random.randint(0, 2)]
#     if player_choice == computer_choice:
#         result = "Match Draw"
#     elif (player_choice == "Rock" and computer_choice == "Scissors") or \
#          (player_choice == "Paper" and computer_choice == "Rock") or \
#          (player_choice == "Scissors" and computer_choice == "Paper"):
#         result = "Player Wins"
#     else:
#         result = "Computer Wins"
    
#     l4.config(text=result)
#     l1.config(text=player_choice)
#     l3.config(text=computer_choice)
#     button_disable()

# # Create labels and buttons
# l1 = tk.Label(root, text="Player", font="normal 20 bold")
# l1.pack(pady=20)

# l2 = tk.Label(root, text="VS", font="normal 20 bold")
# l2.pack(pady=20)

# l3 = tk.Label(root, text="Computer", font="normal 20 bold")
# l3.pack(pady=20)

# l4 = tk.Label(root, text="", font="normal 20 bold")
# l4.pack(pady=20)

# b1 = tk.Button(root, text="Rock", width=20, height=2, command=lambda: determine_winner("Rock"))
# b1.pack(pady=10)

# b2 = tk.Button(root, text="Paper", width=20, height=2, command=lambda: determine_winner("Paper"))
# b2.pack(pady=10)

# b3 = tk.Button(root, text="Scissors", width=20, height=2, command=lambda: determine_winner("Scissors"))
# b3.pack(pady=10)

# reset_button = tk.Button(root, text="Reset Game", width=20, height=2, command=reset_game)
# reset_button.pack(pady=20)

# # Run the main loop
# root.mainloop()
