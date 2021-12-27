"""Number guessing game, guess the number and win
@authors:
Michael Hayes
Theodore Hartin
Nathanael Mottonen
Zachery Brinner
"""
import random
import logging
import re
from datetime import datetime


def logs():
    """Turns debugging on or off
    """
    # Turns debugg logging on/off determined by user input

    loop = True
    while loop:
        try:
            log = ""
            log = input("Would you like logging on Y/N\n")
        except RuntimeError:
            print("error")
            loop = False
        if bool(re.match(r'^(Y)$', log)):
            loop = False
            logging.basicConfig(level=logging.DEBUG)
        elif bool(re.match(r'^(N)$', log)):
            loop = False


def generate_number():
    """ Generates a random number between 1~100
    Returns:
        int: Random Generated integer type
    """
    num = int(random.random()*100//1) + 1
    return num


def get_input(guess_low, guess_high):
    """gathers input from user and prints string to console
    Args:
        guess_low (int): low end of guess
        guess_high (int): high end of guess
    Returns:
        string: the guess the user inputs
    """
    try:
        user_input = input("Guess a number between " + guess_low +
                           "~" + guess_high + "\n")
        logging.debug("\nDate: %s\nInput is: %s",
                      str(datetime.now()), user_input)
        return user_input
    except TypeError:
        print("error")
    return ""


def number_guesser():
    """Main game loop. generates random number
    and allows the user to guess the number.
    Keyword arguments:
    user_input -- number the user guessed
    """
    logs()
    num = generate_number()
    logging.debug("\nDate: %s\nAnswer is: %s",
                  str(datetime.now()), str(num))
    guess = "0"  # number guessed
    guess_high = "100"  # if guess is higher than number
    guess_low = "1"  # if guess is lower than number
    count = 0  # Guess attempts
    # Main game loop when guess is correct loop ends
    try:
        while int(guess) != num:
            user_input = get_input(guess_low, guess_high)
            if not user_input.isdigit():  # used to only take numbers as input
                continue
            count += 1
            logging.debug("\nDate: %s\nCount is: %s",
                          str(datetime.now()), str(count))
            if int(user_input) > num:
                guess = user_input
                # used to only change value if guess is lower than guess_high
                if int(guess_high) > int(user_input):
                    guess_high = user_input
                    print("Too high!!")
            elif int(user_input) < num:
                guess = user_input
                # used to only change value if guess is higher than guess_low
                if int(guess_low) < int(user_input):
                    guess_low = user_input
                    print("Too low!!")
                # if guess is correct ends loop and prints win text
            elif int(user_input) == num:
                guess = user_input
                print("Congratulations!! You Win!\nAmount of Tries: " +
                      str(count))
    except RuntimeError:
        print("error")

number_guesser()
