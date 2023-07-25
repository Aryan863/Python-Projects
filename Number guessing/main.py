from art import logo
import random

def set_difficulty():
    '''Set the difficulty according to user input
    returns- difficulty level'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'- ")

    if difficulty == "easy":
        return 10
    else :
        return 5

def check_number(number,guess,attempts):
    if guess == number:
        print(f"You got it right!!!. The number was {number}")
    elif guess>number:
        print("Too high ")
        print(f"You have {attempts-1} attempts remaining")
        return attempts-1     
    elif guess<number:
        print("Too low ")
        print(f"You have {attempts-1} attempts remaining")
        return attempts-1

    


def game_start():
    print(logo)
    print("Welcome to number guessing game\nI am think of a number between 1 and 100 ")
   
    number = random.randint(1,100)
    attempts = set_difficulty()
    guess=-1

    while guess != number:
        if attempts==0:
            print("You ran out of chances. you lose!! ")
            break
        elif number == guess:
            break
        guess = int(input("Enter your guess- "))
        attempts=check_number(number, guess, attempts)


end = False
while not end:
    game_start()
    cont = input("Do you want to play again? 'y' or 'n'- ")
    if cont == 'n':
        print("Thanks for playing!!!")
        end = True

    