#Amy Griesmeyer
#march 30. 2024
#guessNumber.py


##import random
##def display_title():
##	Display Intro   
##def getGuess(FIRST,LAST):
##    Prompt for guess
##    while loop to validate that guess is between FIRST and LAST
##    return guess
## 
##def guessWIN(number,guess):
##    Multi-way if statement to determin if number == guess, is too high or too low
##   
##def main():
##    Declare and initialize variables
##    #int rounds, guess, number
##    guess = number = 0
##    playAgain = “y”
##    Invoke display_title() function
##
##    while playAgain == “y” or playAgain == “Y”:
##    rounds = 1
##    Generate random number between 1 and 100
##      
##    while rounds <=7 and guess != number:
##        Display round
##        Call getGuess() and store result in guess 
##              Call guessWin()
##              Add to round counter
##	    Prompt user to play again

#Import random
import random

##def display_title():
##	Display Intro 
def display_title():
    print("\nGuess the Mystery Number...")
    
##def getGuess(FIRST,LAST):
##    Prompt for guess
##    while loop to validate that guess is between FIRST and LAST
##    return guess
def get_guess(first, last):
    while True:
        try:
            guess = int(input(f"Enter your guess ({first} - {last}): "))
            if first <= guess <= last:
                return guess
            else:
                print(f"Error...Incorrect number. Try again.")
        except:
            print("Error...Incorrect number. Try again")

##def guessWIN(number,guess):
##    Multi-way if statement to determin if number == guess, is too high or too low
def guess_win(number, guess):
    if guess == number:
        print("\nCongratulations! You guessed the mystery!")
        return True
    elif guess < number:
        print(f'---> {guess} is too low...')
    else:
        print(f'---> {guess} is too high...')
    return False

##def main():
##    Declare and initialize variables
def main():
    play_again = "y"
    display_title()

##    #int rounds, guess, number
##    guess = number = 0
##    playAgain = “y”
##    Invoke display_title() function
    while play_again.lower() == "y":
        rounds = 1
        number = random.randint(1, 100)

        while rounds <= 7:
            print(f"\nRound {rounds} of 7:")
            print("----------------------------")
            guess = get_guess(1, 100)
            if guess_win(number, guess):
                break
            rounds += 1

##  Prompt user to play again
        play_again = input("Do you want to play again? (y/n): ")

#thank user for playing
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

    
