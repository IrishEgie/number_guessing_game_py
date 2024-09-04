import art 
import random as rd

def num_guess(rd_num, lives):

    while lives!=0:
        guess = input("Make a guess: ")
        
        if int(guess) >rd_num:
            print("Too High.\nGuess Again.")
            
        elif int(guess)<rd_num:
            print("Too Low.\nGuess Again.")
        else: 
            print(f"You got it! The answer was {rd_num}.")
            return
            
        lives-=1    
        print(f"You have {lives} attempts remaining to guess the number.")
    return lives

#intro
print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

diff = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

#life counter
if diff == "easy":
    life = 10
else:  
    life = 5
print(f"You have {life} attempts remaining to guess the number.")

random_num = rd.randint(1,100)

num_guess(int(random_num),life)