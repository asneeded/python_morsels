import random

number = random.randint(0,101)

choice = input("Guess a number (0-100): ")

def check_num(choice):
    if number > choice:
        print("too low")
    elif number < choice:
        print("too high")
    elif number == choice:
        print(f"Just Right! {choice}")
        return True

while True:
    choice = input("Guess a number (0-100): ")
    