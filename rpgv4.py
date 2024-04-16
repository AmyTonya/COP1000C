#random

#Group 2 Project file name: rpgv1.py
#Names: Amy Griesmeyer and Sean Wilkie
#date: February 18, 2024
#Design your own music festival

##Version 1 pseudocode
#Design your own music festival
#define main
#display an intro on the opening page
#display the main menu: 1) see rules 2)Play Game 3)Exit
#prompt user for his/her name
#prompt user for the main menu choice
#Display the rules for the game
#display the story line
#thank the user for playing
#include documentation (comments) in code

##Version 2 Pseudocode
##define variables
##if elif else
##f string for each display for choice
##assign variable to main menu choice
##Main menu display when rules are selected
##display error when invalid selection is given
##main menu display when play game is selected
##assign points to each selection in story line
##season: summer 100 winter 200 fall 300 spring 400
##location: ciy 100 farm 200 beach 300 stadium 400
##genre: rock 100 pop 200 edm 300 funk 400 all of them 500
##display total score for all selections using f string
##display goodbye to user adding fest name given

##V3 feedback
##I FIXED THIS: Your last if condition can just be else:
##In your next version, please add more to your story line.

#version 3 pseudo
#ranom number generator 1,101
#season points +=
#print total points earned from generator
#location points +=
#print total points earned from generator
#type of music points
#print total points earned from generator
#outfit night points
#print total points earned from generator

def greeting (name):
    print("Hello,", name+"! Your first task will be to name your festival!")
    
def welcome():
    print("WELCOME TO THE BUILD YOUR OWN MUSIC FESTIVAL GAME! LET'S DANCE!\n"
        "Please choose from the following menu:\n"
        "1) See Rules\n2) Play Game\n3) Exit")
    
def final_points(fest_points, location_points, genre_points, outfit_points):
    #a function which returns with a value
    total_points = fest_points + location_points + genre_points + outfit_points
    print(f'You have earned a total of {total_points} points from your choices.\n')
    return total_points

def name():
    #a function with parameters
    name = input('Please enter your name here: \n')
    print("Hello," ,name+"!", "Your first task will be to name your Festival!")
    #space
    print()

#define main
def main():
    # display an intro
    welcome()

    menu_choice = 1

    while menu_choice != 2:
        #enter input for user choice
        menu_choice = int(input("Please enter your choice here: "))
        # Invalid choice response
        while menu_choice < 1 or menu_choice > 3:
            print("Party foul! Please choose from the following menu options!\n")
            print(welcome)
        # 1)print rules selection
        if menu_choice == 1:
            print("You have chosen to see the rules. In this game, you will be given a\n"
              "series of menu choices to select from to plan your ideal music festival.\n"
              "You will be awarded different point values based on your selections.\n"
              "Have fun and get ready to PARTY!\n")
            # display an intro
            welcome()
        elif menu_choice == 3:
            # If user selects 3, - Exit game selection
            print("Why don't you want to party?! \n")

    #If user selects 2, - Start game selection
    #accumulator for total points
    total_points = 0

    print("\nLETS GET PARTYING!\n")
    #Starting with prompting the user for their name
    
    #Print welcome to the game and input for name
    user_name = input('Please enter your name here: ')
    #calling 
    greeting(user_name)
    fest_name = input("\nPlease enter your festival name: ")
    #space
    print()

    #season selections for festival game
    print("What season would you like to attend?")
    print("1) Summer\n"+"2) Winter\n"+"3) Fall\n" +"4) Spring")
    fest_season = input("Enter your season choice: ")
    fest_points = 0
    if fest_season == '1':
        fest_points += 100
        summer = print(f'You have chosen Summer! You have earned {fest_points} points!')
    elif fest_season == '2':
        fest_points += 200
        winter = print(f'You have chosen Winter! You have earned {fest_points} points')
    elif fest_season == '3':
        fest_points += 300
        fall = print(f'You have chosen Fall! You have earned {fest_points} points')
    elif fest_season == '4':
        fest_points += 400
        spring = print(f'You have chosen Spring! You have earned {fest_points} points')
    else:
        print('Invalid selection. Please choose from 1-4.')
    #Space
    print()
    # Update total points accumulator
    total_points += fest_points
    print("Total points earned =" ,total_points)


    #space
    print()

    #Location for festival
    print("Where would you like to have your festival?")
    print("1) Major City\n"+"2) Isolated Farmland\n"+"3) Popular Beach Destination\n"
          +"4) Stadium Atomsphere")
    fest_location = input("Enter your desired festival location: ")
    location_points = 0
    if fest_location == '1':
        location_points += 100
        city = print(f'You have chosen Major City! You have earned {location_points} points!')
    elif fest_location == '2':
        location_points += 200
        farmland = print(f'You have chosen Isolated Farmland! You have earned {location_points} points')
    elif fest_location == '3':
        location_points += 300
        beach = print(f'You have chosen Popular Beach Destination! You have earned {location_points} points')
    elif fest_location == '4':
        location_points += 400
        stadium = print(f'You have chosen Stadium Atomsphere! You have earned {location_points} points')
    else:
        print('Invalid selection. Please choose from 1-4.')
    #space
    print()
    # Update total points accumulator
    total_points += location_points
    print("Total points earned =" ,total_points)
    #space
    print()

    #type of Music
    print("What genre of music will be featured?")
    print("1) Rock\n"+"2) Pop\n"+"3) EDM\n" +"4) Funk\n" +"5) I WANT IT ALL")
    fest_genre = input("Enter the type of music you want to listen to: ")
    genre_points = 0
    if fest_genre == '1':
        genre_points += 100
        rock = print(f'You have chosen Rock Genre! You have earned {genre_points} points!')
    elif fest_genre == '2':
        genre_points += 200
        pop = print(f'You have chosen Pop Genre! You have earned {genre_points} points')
    elif fest_genre == '3':
        genre_points += 300
        edm = print(f'You have chosen Funk Genre! You have earned {genre_points} points')
    elif fest_genre == '4':
        genre_points += 400
        funk = print(f'You have chosen Funk Genre! You have earned {genre_points} points')
    elif fest_genre == '5':
        genre_points += 500
        print(f'YOU WANT IT ALL! You have earned {genre_points} points')
    else:
        print('Invalid selection. Please choose from 1-5.')
    #space
    print()
    # Update total points accumulator
    total_points += genre_points
    print("Total points earned =" ,total_points)


    #Theme night addition
    print("\nWhat theme night outfit do you want?")
    print("1) Group Onesie's \n"+"2) Minions \n"+"3) 5K Participants \n" +"4) Big Lebowski")
    fest_fit = input("Enter your choice of the theme night outfit: ")
    outfit_points = 0
    if fest_fit == '1':
        outfit_points += 100
        onsies = print(f'You have chosen Group Onesies! You have earned {outfit_points} points!')
    elif fest_fit == '2':
        outfit_points += 200
        minion = print(f'You have chosen Minions! You have earned {outfit_points} points')
    elif fest_fit == '3':
        outfit_points += 300
        fiveK = print(f'You have chosen 5K Participants! You have earned {outfit_points} points')
    elif fest_fit == '4':
        outfit_points += 400
        BigLebowski = print(f'You have chosen Big Lebowski! You have earned {outfit_points} points')
    else:
        print('Invalid selection. Please choose from 1-5.\n')
    # Update total points accumulator
    total_points += genre_points
    print()

    final_points(fest_points, location_points, genre_points, outfit_points)



    #thank them for playing
    print(fest_name+ ' is looking great! Thanks for playing!')


if __name__ == '__main__':
    main()
