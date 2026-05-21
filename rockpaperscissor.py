import time
import random

while True:
    user_play = input("Rock, Paper, or Scissors (r/p/s)?: \n").lower().strip()
    
    random_play = random.randint(1, 3)
    
    # 1 - Rock
    # 2 - Paper
    # 3 - Scissors
    
    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    
    print("Shoot!\n")
    
    time.sleep(0.5)
    
    print("=== Result ===")
    
    if random_play == 1:
        print("Computer's choice: Rock")
    elif random_play == 2:
        print("Computer's choice: Paper")
    elif random_play == 3:
        print("Computer's choice: Scissors")
    
    if user_play == "r":
        if random_play == 1:
            print("Tie!")
        if random_play == 2:
            print("You lose!")
        if random_play == 3:
            print("You win!")
    
    elif user_play == "p":
        if random_play == 1:
            print("You win!")
        if random_play == 2:
            print("Tie!")
        if random_play == 3:
            print("You lose!")
    
    elif user_play == "s":
        if random_play == 1:
            print("You lose!")
        if random_play == 2:
            print("You win!")
        if random_play == 3:
            print("Tie!")
    else:
        print("Please enter a valid input!")
    
    if user_play in ["r", "p", "s"]:
        
        user_again = input("Would you like to play again? (y/n): ").strip().lower()
        
        
        if user_again in ["y", "yes", "yep", "yah"]:
            print("==========")
            pass
        elif user_again in ["n", "no", "nah", "no way", "nope"]:
            print("Thanks for playing!")
            break
        else:
            print("I'm going to take that as a no...")
            print("Byeeeeee!")
            break

# Created May 21st, 2026
# Last edited: May 21st, 2026
# This code was created to compare the style of writing code between me and my friend :D
