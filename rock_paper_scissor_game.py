# Rock pape scissor game using a python code...!

import random 
item_list = ["Rock","paper","scissor"]

user_choice = input("Enter your move = Rock, paper, scissor = ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choose same : = Match Tie")

elif user_choice == "Rock" :
    if comp_choice == "paper":
        print ("Paper covers Rock = Computer Win")

    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "paper":
    if comp_choice == "Rock":
        print ("Paper covers Rock = You Win")

    else:
        print("Scissor cut the Paper = Computer win")

elif user_choice == "Scissor":
    if comp_choice == "paper":
        print ("Scissor cuts Paper = You win")

    else:
        print("Rock smashes Scissor = Compurt win")
