#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    counter = 0
    while counter < 5:
        try:
            guess= int(input("Guess a number between 1 and 100: "))
        except ValueError:
            guess = input("Press q to quit, otherwise, press enter to continue: ").lower()
            if guess == "q":
                quit()
            else:
                continue
        else:
            counter += 1
            if guess > num:
                print("Too high!")

            elif guess < num:
                print("Too low!")

            else:
                print("Correct!")
                break

main()
