import random
print("Welcome to the Dice Rolling Game!")
# loop until a 6 is rolled
while True:
    # prompt the user to roll the dice
    input("Press enter to roll the dice...:")
    # roll the dice for the user and computer
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    # print the rolls
    print("You rolled:", user_roll)
    print("The computer rolled:", computer_roll)
    # check if a 6 was rolled
    if user_roll == 6 or computer_roll == 6:
        break
    # determine the winner
    if user_roll == 6 and computer_roll != 6:
        print("Congratulations, you win!")
    elif user_roll != 6 and computer_roll == 6:
        print("Sorry, the computer wins!")
    else:
        print("It's a tie!")
