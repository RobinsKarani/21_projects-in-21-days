import random

def play_game():
    guesses = 0
    random_number = random.randint(30, 40)  # Random number between 30 and 40
    max_guesses = 4
    
    print("****Welcome to the Guessing Game!****")
    
    while guesses < max_guesses:
        guess = float(input(f"Guess a number (30-40): "))  #Prompt user for guess
        
        guesses += 1  #increment guesses counter

        if guess == random_number:
            print("You're Correct!!!")
            print(f"It took you {guesses} guesses.")
            Option2 = input("Do you want to play again? (Y/N): ").upper()
            if Option2 == "N":
                print("**Game Ended**")
                break
            else:
                play_game()  #restart the game if user chooses to play again
                break
        else:
            print("Try again!")
            print(f"You have {max_guesses - guesses} guesses left.")
        
    #if user runs out of guesses
    if guesses == max_guesses and guess != random_number:
        print(f"Sorry! You've used all {max_guesses} guesses. The correct number was {random_number}.")
        Option2 = input("Do you want to play again? (Y/N): ").upper()
        if Option2 == "N":
            print("**Game Ended**")
        else:
            play_game()  #Restart the game if user chooses to play again

#Start the game
play_game()
