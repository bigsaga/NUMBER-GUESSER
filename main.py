from colors import *
from random import randint

# welcome to the world of gaming
def welcome_screen():
    print(BLUE, "****** welcome to the world of guessing game **********")
    user_input = int(input(WHITE + "Choose Your Level\n"
                               "1. Normal (1 - 50)\n"
                               "2. Intermediate (1 - 200)\n"
                               "3. Hard (1 - 500)\n"
                               "4. Exit Application\n\n"
                               "Enter Request : "))
    # calling a function and passing user_input to it
    guess_range = user_option(user_input)
    if guess_range != 0:
        generate_random_number(guess_range)

    user_option(user_input)
# user's option
def user_option(user_input):
    guess_range = 0
    if user_input == 1:
        guess_range = 50
    elif user_input == 2:
        guess_range = 200
    elif user_input == 3:
        guess_range = 5000
    elif user_input == 4:
        print("***** Thanks For The Using Our App, Hope To See You Again ****")
        exit(1)
    else:
        print(RED, "Invalid Request, Try Again.")
        return welcome_screen()
    return guess_range


def generate_random_number(guess_range):
    # Generate random number between certain range
    generate_number = randint(1, guess_range)

    # user chances
    user_chance = 4

    for i in range(4):
        user_guess = int(input('Provide Your Guess Number :'))

    # Determine if the guess is correct
        if user_guess == generate_number:
            print(GREEN, f'Hurray!!!!, You Guess Is Correct')
            break
        elif user_guess > generate_number:
            print(YELLOW, ' Your Guess Is Too High, Try Again')
            user_chance -= 1
        elif user_guess < generate_number:
         print(YELLOW, 'Your Guess Too Low, Try Again')
    # reduce the number of chance and prompt user chance lef
        user_chance -= 1
        print(f'Number Of Chance Left Is {user_chance}')


    # inform user of thr correct guess number
    if user_chance == 0:
        print(RED, F'sorry The Correct Guess Is {generate_number}')

welcome_screen()