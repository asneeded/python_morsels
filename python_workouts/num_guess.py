import random
import sys


def guessing_game():
    number = random.randint(0,100)
    while True:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Enter a number 0-100:")
            guessing_game()
        if guess > number:
            print(f"{guess:#>10} is Too high")
        elif guess < number:
            print(f"{guess:#<10} is Too low")
        elif guess == number:
            print(f"{guess:#<5} is Just right")
            sys.exit()

if __name__ == "__main__":
    guessing_game()