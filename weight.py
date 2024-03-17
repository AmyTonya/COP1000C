#weight.py
#Amy Griesmeyer
#March 15, 2024
#description of program: Active person cuts calorie intake by 500 a day program

##define main
#display intro
##display  menu options
##user input priming read
##validation loop, user must pick from menu choices
##if validation true, continue with menu
##if option 1 is selected; display tips
##Input Validation Loop
##user input priming read
##validation, User must input weight value >= 100
##Prints weight table, 4lbs subtracted from weight each month; user controlled loop
##display weight table for 6 months -4 pounds each month
#if choice is not 1 through 3
##If user selects 3, exit program with message


def main():
    #display intro
    print("\n500 Less a Day Makes the Weight Go Away...\n")
    #Display menu options
    print("Choose one of the following options:")
    print("\t1. Display “10 ways to cut 500 calories” guideline.")
    print("\t2. Generate next semester expected weight table.")
    print("\t3. Quit")
    #User input, priming read
    choice = int(input('Option: '))

    #Validation Loop, user must pick from menu choices
    while choice > 3 or choice < 1:
        print("Error... Invalid option. Try Again.")
        print()
        print("Choose one of the following options:")
        print("1. Display “10 ways to cut 500 calories” guideline.")
        print("2. Generate next semester expected weight table.")
        print("3. Quit")
        choice = int(input("Option: "))
        
    #if validation is true, continue with menu
    else: 
        while choice == 1 or choice == 2:
            #if option 1 is selected; display tips
            while choice == 1: 
                print('\nTry these 10 ways to cut 500 calories every day.')
                print('\t* Swap your snack.')
                print('\t* Cut one high-calorie treat.')
                print('\t* DO NOT drink your calories.')
                print('\t* Skip seconds.')
                print('\t* Make low calorie substitutions.')
                print('\t* Ask for a doggie bag.')
                print('\t* Just say “no” to fried food.')
                print('\t* Build a thinner pizza.')
                print('\t* Use a smaller plate.')
                print('\t* Avoid alcohol.')
                print('Source: US National Library of Medicine\n')

                print("Choose one of the following options:")
                print("\t1. Display “10 ways to cut 500 calories” guideline.")
                print("\t2. Generate next semester expected weight table.")
                print("\t3. Quit")
                choice = int(input("Option: "))
                        
                #Input Validation Loop
                while choice > 3 or choice < 1:
                    print('Error... Invalid option. Try Again.')
                    print()
                    print("Choose one of the following options:")
                    print("\t1. Display “10 ways to cut 500 calories” guideline.")
                    print("\t2. Generate next semester expected weight table.")
                    print("\t3. Quit")
                    choice = int(input("Option: "))

            #if user chooses 2
            while choice == 2:
                #user input priming read
                weight = int(input("\nEnter starting weight in pounds (>=100):  "))

                #validation, User must input weight value >= 100
                while weight < 100: 
                    print('\tError... Invalid weight. Try Again.')
                    weight = int(input("\nEnter starting weight in pounds (>=100):  "))
                    
                #Print weight table, 4lbs subtracted from weight each month
                else: 
                    print('----------------')
                    print('Month    Weight')
                    print('----------------')

                    #display weight table for 6 months -4 pounds each month; user controlled loop
                    for month in range(1,7):
                        print(f'  {month}      {weight - 4} lbs')
                        weight -=4
                    else:
                        print("\nChoose one of the following options: ")
                        print("\t1. Display “10 ways to cut 500 calories” guideline.")
                        print("\t2. Generate next semester expected weight table.")
                        print("\t3. Quit")
                        choice = int(input("Option: "))    
                        
                    #if choice is not 1 through 3
                    while choice > 3 or choice < 1:
                        print("\tError... Invalid option. Try Again")
                        print()
                        print("Choose one of the following options:")
                        print("\t1. Display “10 ways to cut 500 calories” guideline.")
                        print("\t2. Generate next semester expected weight table.")
                        print("\t3. Quit")
                        choice = int(input("Option: "))
                        
        #If user selects 3, exits program
        else:
            print("\nGood Bye...")       
main()
