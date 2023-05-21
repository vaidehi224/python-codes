import random
print("Welcome to Rock, Paper, Scissors!")
# define the options
options = ["rock", "paper", "scissors"]
# loop until the user decides to quit
while True:
    # get the user's choice
    user_choice = input("Enter rock, paper, scissors, or q to quit: ").lower()
    # check if the user wants to quit
    if user_choice == "q":
        print("Thanks for playing!")
        break
    # check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice, please try again.")
        continue
    # generate the computer's choice
    computer_choice = random.choice(options)
    # print the choices
    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)
    # determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or\
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("The computer wins!")
