def ticketcostcalculator():
    try:
        age = int(input("Enter your age: "))
        ticketcost = 0
        if age < 12:
            ticketcost = 5
        elif age >= 12 and age < 18:
            ticketcost = 7
        else:
            ticketcost = 10

        print(f"Your ticket cost £{ticketcost}")
    except:
        print("Your input must be a number.")
    finally:
        pass

import random

def rockpaperscissors():
    userchoice = input("Enter your move (rock, paper, scissors): ")
    possiblechoices = ["rock", "paper", "scissors"]
    compchoice = random.choice(possiblechoices)
    res = " "
    if (userchoice.lower() == "rock" and compchoice == "paper") or (userchoice.lower() == "paper" and compchoice == "scissors") or (userchoice.lower() == "scissors" and compchoice == "rock"):
        res = "The computer won!"
    elif (compchoice.lower() == "rock" and userchoice == "paper") or (compchoice.lower() == "paper" and userchoice == "scissors") or (compchoice.lower() == "scissors" and userchoice == "rock"):
        res = "You won!"
    elif userchoice.lower() != "rock" and userchoice.lower() != "paper" and userchoice.lower() != "scissors":
        res = "You must input either rock, paper or scissors."
    else:
        res = "It's a tie!"

    print(f"You chose: {userchoice}\nComputer chose: {compchoice}\n{res}")
    pass


def testscorecalc():
    try:
        testscore = int(input("Enter the student's score (0-100): "))
        grade = " "
        if testscore >= 0 and testscore <= 100:
            if testscore < 60:
                grade = "F"
            elif testscore >=60 and testscore < 70:
                grade = "D"
            elif testscore >= 70 and testscore < 80:
                grade = "C"
            elif testscore >= 80 and testscore < 90:
                grade = "B"
            else:
                grade = "A"

            print(f"The student's grade is: {grade}")
        else:
            print("The student's score must be between 0 and 100.")
    except:
        print("Your input must be a number.")
    finally:
        pass

try:
    whatprogram = int(input("What program would you like to run? (1,2 or 3) "))

    if whatprogram == 1:
        ticketcostcalculator()
    elif whatprogram == 2:
        rockpaperscissors()
    elif whatprogram == 3:
        testscorecalc()
    else:
        print("You did not input 1, 2 or 3.")
except:
    print("Please input 1, 2 or 3.")