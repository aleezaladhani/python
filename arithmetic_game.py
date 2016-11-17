# Game to test either multiplication or addition

from random import randint

def perform_test(arithmetic_operation, n):
    '''
    (number, number) --> number
    Returns the number of correct answers the student calculated when answering questions with length of the inputted value and of the preferred form that is inputted as well.
    '''
    
    i=0
    correct_answers=0
    
    for num in range (i,n,1):
        a=randint(0,9)
        b=randint(0,9)

        if arithmetic_operation==0:
            question=int(input(str(a)+" + "+str(b)+" = "))
            if question==(a+b):
                correct_answers=correct_answers+1
            else:
                print("Incorrect - the answer is "+str(a+b))
                correct_answers=correct_answers

        if arithmetic_operation==1:
            question=int(input(str(a)+" * "+str(b)+" = "))
            if question==(a*b):
                correct_answers=correct_answers+1
            else:
                print("Incorrect - the answer is "+str(a*b))
                correct_answers=correct_answers

    return correct_answers


# Main Function

n=int(input("Welcome to the addition/multiplication test!\n\nHow many questions would you like to be tested on?\n\tPlease enter a non-negative integer for the answer: "))
if n<=0:
    print("Good Bye")
else:
    print("This software tests you with", n, "questions.\n")
    arithmetic_operation=int(input("What form of arithmetic operation would you like to be tested on?\n\t0) Addition\n\t1) Multiplication\nPlease make a selection(0 or 1): "))

    correct_answers=perform_test(arithmetic_operation, n)

    percentage=(correct_answers/n)*100

    if percentage>=80:
        print("Well done! Congratulations.")
    elif percentage>=60:
        print("Not too bad but please study and practice some more.")
    else:
        print("Please study more and ask your teacher for help.")


