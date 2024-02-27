##roulette.py
##Amy Griesmeyer
##february 26, 2024
##description of program: enter a pocket number
##and displays whether the pocket is green, red, or black.

##Pseudocode:
##decalre and initalize variables
##int numbers from prompt
##elif if else for number ranges
##define main function
##display intro
##prompt user to enter a pocket number
##pocket 0 is green
##pockets 1 through 10 odd are red black are even
##pockets 11 through 18 odd are black even are red
##pockets 19 through 28 off are red black are even
##pockets 29 through 26 odd are black even are red
##display color of number selection 
##if prompt is out of range display invalid statement number must be between  
##0 through 36


##define main function
def main():
    
##display intro
    print('Roulette Wheel Colors App...\n')
##prompt user to enter a pocket number
    number = int(input('Please enter pocket number (0-36):  '))

    if number >=-0 and number <=36:
        
##pocket 0 is green
        if number == 0:
            color = 'green'   
##pockets 1 through 10 odd are red even are black 
        elif number >= 1 and number <= 10:
            if number % 2 == 0:
                color = 'black'
            else:
                color = 'red'            
##pockets 11 through 18 odd are black even are red
        elif number >= 11 and number <= 18:
            if number % 2 == 0:
                color = 'red'
            else:
                color = 'black'            
##pockets 19 through 28 odd are red even are black
        elif number >= 19 and number <= 28:
            if number % 2 == 0:
                color = 'black'
            else:
                color = 'red'
##pockets 29 through 36 odd are black even are red
        elif number >= 29 and number <= 36:
            if number % 2 == 0:
                color = 'red'
            else:
                color = 'black'
        print()
        print(f'The color of the Wheel Pocket is {color}.')
##if prompt is out of range display invalid statement number must be between  
##0 through 36
    else:
        print('\tError...Invalid Pocket. Try again.')
        

       
main()

        

    
