import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
chosen_word=random.choice(word_list)

# Initialise the guess list with '_'
guess=[]
for letter in chosen_word:
    guess+='_'

def printGuess():
    for i in guess:
        print(i,end=" ")


life=7
hang=-1
while(life>0):
    user_letter=input("\nEnter a letter- ").lower()
    print("")
    printGuess()

    if user_letter in guess:
        print(f"You've already guessed {user_letter}")
        continue

    flag=0
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if user_letter==letter:
            guess[i]=user_letter
            flag=1
    
    printGuess()
    
    if flag==0:
        print(stages[hang])
        hang-=1
        print("\nChoose another letter\nYou have lost 1 life")
        life-=1
    
    str=""
    for ak in guess:
        str+=ak
    
    if str==chosen_word:
        print(f"Game won\nchosen word- {str}")
        break

if(life==0):
    print("Sorry you lost. Better luck next time!!!")
    print(f"The correct word was- {chosen_word}")
