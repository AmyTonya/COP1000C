#program name: labassignment1.py
#name: Amy Griesmeyer
#date: January 31, 2024
#Description of program: MadLib Game

#define a main function: input output using print and input commands
def main():
    
    #Use the print function to display an intro on the screen 
    print("Welcome to the MadLib games!")
    #skip a line
    print()

    #Use print function to display directions to fill out questions
    print("Enter the following words:")

    #Use the input command to prompt user for game questions
    PNOUN1 = input("Plural noun: ")
    FNAME = input("Person's First Name: ")
    NOUN1 = input("Noun: ")
    LNAME = input("Person's Last Name: ")
    PNOUN2 = input("Plural Noun: ")
    PLACE1 = input("Place: ")
    PNOUN3 = input("Plural Noun: ")
    PLACE2 = input("Place: ")
    PNOUN4 = input("Plural Noun: ")
    NOUN2 = input("Noun: ")
    ADJECTIVE1 = input("Adjective: ")
    ADJECTIVE2 = input("Adjective: ")
    VERB = input("Verb: ")
    ADJECTIVE3 = input("Adjective: ")

    #skip a line
    print()
    #Enter The Big Game to introduce the game below
    print("The Big Game!!!")
    #skip a line
    print()
    
    #Use Print to display the answers in a story given from the input 
    print("Hello there, sports", PNOUN1 + "!")
    print("This is", FNAME + ", talking to you from the press " + NOUN1)
    print("in", LNAME + " Stadium, where 57,000 cheering " + PNOUN2)
    print("have gathered to watch (the) " + PLACE1 , PNOUN3)      
    print("take on (the)", PLACE2, PNOUN4 + ".")
    print("Even though the " + NOUN2, "is shining, it's a/an " + ADJECTIVE1)
    print("cold day with the temperature in the", ADJECTIVE2 + " 20s.")
    print("We'll be back for the opening", VERB + "-off after a few words")
    print("from our " + ADJECTIVE3, "sponsor.")
  
