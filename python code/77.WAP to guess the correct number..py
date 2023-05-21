import random
# generate a random number between 1 and 100
secret_number = random.randint(1, 100)
# initialize the number of guesses
num_guesses = 0
while True:
    # get a guess from the user
    guess = int(input("Guess a number between 1 and 100: ")) 
    # increment the number of guesses
    num_guesses += 1 
    # check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations, you guessed the number in {num_guesses} guesses!")
        break 
    # give the user a hint
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
