#Amy Griesmeyer
#April 15, 2024
#quizGrade.py


#defines a function to line of - 40 times
#Answer key to the quiz
#defines the main function of this program
#used to restart the program loop later
#error handling if no error excutes the following code
#Sets variable used later to tally answers and grade quiz
#intro
#user input for student name and file name
#opens file using the user input for reading
#reads the answers from the file and copys them into a new list
#compares the new list of answers to the answer key
#header information using student name input
#calls line function
#display correct, incorrect answer total along with which question was wrong
#calculate student grade
#if the student results above 60% they pass
#more lines
#ask if user wants to grade another quiz
#error handling shows what the error is and restarts program
#once the user chooses n
#calls the main function to run

import time
#defines a function to line of - 40 times
def line():
    print('-' * 40)
#Answer key to the quiz 
ANSWERKEY = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'D', 'B']

#defines the main function of this program
def main():
    #used to restart the program loop later 
    again = 'y'
    while again == 'y' or again == 'Y':
        #error handling if no error excutes the following code
        try:
            #Sets variable used later to tally answers and grade quiz
            correctCounter = 0
            incorrectCounter = 0
            studentAnswers = []
            incorrectAnswers = []
            
            #intro
            print("Quiz Grading App...")
            #user input for student name and file name 
            studentName = input('Enter name of student: ')
            selectedFile = input('  \"   quiz answers file: ')
            #opens file using the user input for reading
            with open(f'{selectedFile}', 'r') as file:
                #reads the answers from the file and copys them into a new list 
                answers = file.readline().strip()
                while answers != '':
                    studentAnswers.append(answers)
                    answers = file.readline().strip()
                #compares the new list of answers to the answer key
                for i in range(len(ANSWERKEY)):
                    if studentAnswers[i] == ANSWERKEY[i]:
                        correctCounter += 1
                    else:
                        incorrectCounter += 1
                        incorrectAnswers.append(i +1)
                #header information using student name input
                print()
                print(f'{studentName} Quiz Results')
                #calls line function
                line()
                #display correct, incorrect answer total along with which question was wrong
                print(f'Correct Answers: {correctCounter}')
                print(f'Incorrect Answers: {incorrectCounter} {incorrectAnswers}\n')
                #calculate student grade
                totalQuestions = correctCounter + incorrectCounter
                grade = int((correctCounter / totalQuestions) * 100)
                #if the student results above 60% they pass 
                if grade >= 60:
                    print(f'{studentName} PASSED the quiz.')
                else:
                    print(f'{studentName} FAILED the quiz.')
                #more lines
                line()
                #ask if user wants to grade another quiz  
                again = input('Do you have another student (y/n): ')
        #error handling shows what the error is and restarts program        
        except Exception as error:
            print(f'\nERROR... could not process {selectedFile}')


    #once the user chooses n
    else:
        print('Good Bye!')

#calls the main function to run
if __name__ == "__main__":
    main()
