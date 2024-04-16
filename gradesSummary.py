#Amy Griesmeyer
#April 5, 2024
#gradesSummary.py
#Course grades summary report based on course information stored in COP1000C.txt


#defines a function to print 70 '-' on one line
#defines a function take file object and call read line and strip()
#define the main function of the program
#user input if they wish to continue using the program
#error handling, if no error 
#assigning value to global variables 
#take user input for file name , pass input to open file in read  mode
#header 
#reads and displays first line
#reads and displays second and third line
#header for student and grade
#call more lines from the file to use for loop
#while for more information to be read, loop iterates
#format grade into int value
#if grade is passing, add one to passing value
#if grade is failing,add one to failing
#count for number of students
#while loop adds the value of the grade to the gradeSum var
#display student name and grade
#new lines for new student loop
#header after loop stops iterating
#display value of passing and failing students along with % of passing students
#display average grade
#input if user wants to process another file
#error display what the error is and calls the main function 
#if user did not enter a 'y' for the input then program displays goodbye 
#call to the main function


import time

#defines a function to print 70 '-' on one line
def linePrint():
    print('-' * 42)
#defines a function take file object and call readline and strip()
def newLine(data):
    return data.readline().strip()
#define the mainfunction of the program
def main(): 
    #user input if they wish to continue using the program
    another = 'y'
    while another == 'y' or another == 'Y':
        #error handling, if no error 
        try:
            #assigning value to global variables 
            passing = 0
            failing = 0
            students = 0
            gradeSum = 0

            #take user input for file name, pass that input to open file object in read mode
            course = input('Enter name of course file: ')
            with open(f'{course}', 'r') as file:
                #header
                print('-' * 70)
                print(f'{"Broward College Grades Summary":^70}')
                print('-' * 70)
                #reads and displays first line
                course = newLine(file)
                print(f'{course}')
                #read and display second and third line
                professor = newLine(file)
                term = newLine(file)
                print(f'Professor: {professor:<30}', f'Term: {term:>}\n')
                #header for student and grade
                print(f'{"Student Name":<20}', f'{"Grade":^30}')
                linePrint()
                #call more lines from the file to use for loop
                name = newLine(file)
                grade = newLine(file)
                #while for more information to be read, loop iterates
                while name != "" or grade != "":
                    #format grade into a int value 
                    gradeInt = int(grade)
                    #if grade is passing add, 1 to passing value
                    if gradeInt >= 60:
                        passing += 1
                    #if grade is failing add, 1 to failing value
                    else:
                        failing += 1 
                    #count for number of students
                    students += 1
                    #while loop adds the value of the grade to the gradeSum var
                    gradeSum += gradeInt 
                    #display the student name and grade
                    print(f'{name:<20}', f'{grade:^30}')
                    #new lines for a new student loop
                    name = newLine(file)
                    grade = newLine(file)
                #header after loop stops iterating
                print('\nStudents\' Performance')
                linePrint()
                #display value of passing and failing students along with % of passing students
                print(f'Passed: {passing:<20}', f'Failed: {failing}')
                passPercentage = (passing / students) * 100
                print(f'Passing Percent: {passPercentage:.0f}%')
                #display average grade 
                gradeAvg = gradeSum / students
                print(f'Average Grade: {gradeAvg:.0f}\n')
                #input if user wants to process another file
                another = input('Would you like to process another file (y/n)')
        #error display what the error is and calls the main function        
        except Exception as error:
            print(f'\nError... {course} file not found.')

            main()
    #if user did not enter a 'y' for the input then program displays goodbye     
    else:   
        print("\nGood Bye.")
        time.sleep(2)
#call the main function
if __name__ == '__main__':
    main()
