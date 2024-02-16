#program name: restaurant.py
#Amy Griesmeyer
#February 14, 2024
#Description of program: Restaurant Bill Generator

##Restaurant bill generator
##Define main function
##Use the print function to display program
##promt user to input cost of the food and drinks
##display restaurant bill and enter a line under 
##declare float variables for calculation tax 7.5 tip 18%
##Create Restaurant print using variables to two decimals
##line above total
##display total for restaurant bill to two decimals


#define a main function. 
def main():
    #Use the print function to display program
    print("Restaurant Bill Generator... \n")

    #promt user enter the cost of the food and drinks
    food = float(input("Please enter cost of food:\t"))
    drinks = float(input(" \"\t\"    cost of drinks:\t"))

    #skip a line
    print()
    
    #display restaurant bill and enter a line under 
    print("Restaurant Bill")
    print("------------------------------")

    #skip a line
    print()

    #declare float variables used for bill calculation tax 7.5 tip 18%
    meal = float(food + drinks)
    tax = float(meal * 0.075)
    tip = float((meal + tax) * 0.18)
    total = float(meal + tax + tip)

    #Create Restaurant print using variables to 2 decimals
    print(f'Cost of Meal:\t$\t{meal:.2f}')
    print(f'Tax Amount:\t$\t { tax:.2f}')
    print(f'Tip Amount:\t$\t { tip:.2f}')
    
    #print a line above total
    print("\t\t---------------")

    #display total for restaurant bill to two decimals
    print(f'Total:\t\t$\t{total:.2f}')

    
    
    

    
    
