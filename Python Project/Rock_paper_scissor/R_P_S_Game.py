# import random

# user_input = input("Enter action :")
# possible_action = ["Rock","Paper","Scissor"]
# computer_action = random.choice(possible_action)

# print(computer_action)

# if user_input == computer_action:
#     print("Both the actions are same. Its a tie!")
# elif user_input == "Rock":
#     if computer_action == "Scissor":
#         print ("Rock smashes Scissor, YOU WIN")
#     else:
#         print ("Paper covers Rock, You Lose")
# elif user_input == "Paper":
#     if computer_action == "Rock":
#         print("Paper covers the rock, You Win")
#     else:
#         print("Scissor cut the paper, You Lose")
# elif user_input == "Scissor":
#     if computer_action == "Paper":
#         print("Scissor Cuts the paper, You Win")
#     else:
#         print("Rock smashes the scissor, You Lose")


import random

def get_user_choice ():
    while True:
        choice = input("Enter the choice(rock/paper/scissor)").lower()
        if choice in ["rock", "paper", "scissor"]:
            return choice
        print ("Invalid choice. Try again.")
def get_computer_choice():
    return random.choice(["rock","paper","scissor"])

def dertermine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif(
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You Win"
    else:
        return "Computer Wins"
    
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print (f"You choose {user_choice}")
        print (f"Computer choose {computer_choice}")

        result = dertermine_winner(user_choice, computer_choice)
        print (result)

        if "You Win" in result:
            user_score +=1
        elif "Computer Wins":
            computer_score += 1
        
        print (f"\n Score - You: {user_score}, Computer {computer_score}")

        play_again = input("\n Do you wants to play again? (Yes/No): ").lower()
        if play_again != "yes":
            break

    print ("\n Thanks for playing")
if __name__ == "_main_":
    print ("Welcome to Rock, Paper, Scissors!")

play_game()