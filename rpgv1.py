#Group 2 Project file name: rpgv1.py
#Names: Amy Griesmeyer and Sean Wilkie
#date: February 18, 2024
#Design your own music festival

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


#define main
def main():
    #display an intro
    print("WELCOME TO THE BUILD YOUR OWN MUSIC FESTIVAL GAME! LET'S DANCE!\n")
  
    #display menu and choices
    print("Please choose from the following menu:")
    print("1) See Rules\n"+"2) Play Game\n"+"3) Exit\n")

    #enter input for user choice
    input("Please enter your choice here: ")
    #space
    print()
    
    #print rules
    print("You have chosen to see the rules. In this game, you will be given a\n"
          "series of menu choices to select from to plan your ideal music festival.\n"
          "You will be awarded different point values based on your selections.\n"
          "Have fun and get ready to PARTY!\n")
    
    #input for user name
    name = input("Please enter your name here: ")
    #add a line
    print()
    
    #Print welcome to the game and input for name
    print("Hello,",name+"!", "Your first task will be to name your festival!")
    fest_name = input("Please enter your festival name: ")
    #space
    print()

    #season for festival
    print("What season would you like to attend?")
    print("1) Summer\n"+"2) Winter\n"+"3) Fall\n" +"4) Spring")
    fest_season = input("Enter your season choice: ")
    #space
    print()

    #Location for festival
    print("Where would you like to have your festival?")
    print("1) Major City\n"+"2) Isolated Farmland\n"+"3) Popular Beach Destination\n"
          +"4) Stadium Atomsphere")
    fest_location = input("Enter your desired festival location: ")
    #space
    print()
    
    #type of Music
    print("What genre of music will be featured?")
    print("1) Rock\n"+"2) Pop\n"+"3) EDM\n" +"4) Funk\n" +"5) I WANT IT ALL")
    fest_genre = input("Enter the type of music you want to listen to: ")
    #space
    print()
    
    #Enter Headliner name
    print("Who will be the headliner?")
    fest_headliner = input("Enter your choice: ")

    #space
    print()
    #thank them for playing
    print(fest_name+" is looking good! Thanks for playing!")

    
