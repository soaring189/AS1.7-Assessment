#Evaluation score. Beautifying output. Add comment.
import random


def NameAgeChecker():
    while True:
        #Input user's name and age
        name = input("Please input your name: ")
        age = input("Please input your age: ")
        #Confirm user's name and age
        confirm = input(f"Name: {name}. Age: {age}. "
                        f"Please enter Yes/No: ").upper()
        #If it's not YES or Y, then loops again until it's YES/Y
        if confirm == "Y" or confirm == "YES":
            break


def If_played_before():
    #Ask user if they played before
    played_before = input("Have you played before?(Y/N)").upper()
    #If user input Y/YES, then pass. If not, print rules
    if played_before == "Y" or played_before == "YES":
        pass
    else:
        Say_rules()


def Say_rules():
    #Print the rules
    print("Welcome to Māori language quiz\n"
          "There are three tests:\n"
          "A:Maori numbers test\n"
          "B:Maori months test\n"
          "C:Maori days test\n"
          "There are ten questions for each test, and you get one point for "
          "each correct answer. See how many points you'll get.")


def Maori_numbers():
    score = 0
    #Loop 10 times
    for i in range(1, 11):
        #Choose a random number
        random_number = random.randint(1, 10)
        #Input user's answer
        user_answer = input(f"What is number{random_number} "
                            f"in Maori language: ").lower()
        #Define the correct answer
        number_list = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu",
                       "waru", "iwa", "tekau"]
        if user_answer == number_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        elif random_number == 4 and user_answer == "wha":
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)\n")
    return score


def Maori_months():
    score = 0
    # Loop 10 times
    for i in range(1, 11):
        # Choose a random number
        random_number = random.randint(1, 12)
        # Input user's answer
        user_answer = input(f"What is the {random_number}th month "
                            f"in Maori language: ").lower()
        # Define the correct answer
        month_list = ["hānuere", "hui tanguru", "poutū", "aperira", "me",
                      "pipiri", "hōngongoi", "awatea", "mahuru",
                      "whiringa-ā-rangi", "whiringa ā-rangi", "haki"]
        month_list1 = ["hanuere", "hui tanguru", "poutu", "aperira", "me",
                       "pipiri", "hongongoi", "awatea", "mahuru",
                       "whiringa-a-rangi", "whiringa a-rangi", "haki"]
        if user_answer == month_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        elif user_answer == month_list1[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)\n")
    return score


def Maori_days():
    score = 0
    # Loop 10 times
    for i in range(1, 11):
        # Choose a random number
        random_number = random.randint(1, 7)
        # Input user's answer
        user_answer = input(f"What is the {random_number}th day in the week "
                            f"in Maori language: ").lower()
        # Define the correct answer
        day_list = ["mane", "tūrei", "te wenerei", "tāite", "paraire",
                    "hātarei", "rātapu"]
        day_list1 = ["mane", "turei", "te wenerei", "taite", "paraire",
                     "hatarei", "ratapu"]
        if user_answer == day_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        elif user_answer == day_list1[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)\n")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)\n")
    return score


def Estimate_score(score):
    #Judgment score
    if score == 0:
        print("Maybe you should learn Māori langauge again.")
    if 0 < score <= 5:
        print("Maybe you need more revision.")
    if 5 < score <= 8:
        print("Good job, You got more than half the score")
    if score == 9:
        print("Great work, you got nearly all correct!")
    if score == 10:
        print("Excellent, you got all correct!")


NameAgeChecker()
If_played_before()
while True:
    #Choose which test to do, if not A/B/C, loop again
    choose_test = input("Which test do you want to choose(A/B/C): ").upper()
    if choose_test == "A":
        Estimate_score(Maori_numbers())
        break
    elif choose_test == "B":
        Estimate_score(Maori_months())
        break
    elif choose_test == "C":
        Estimate_score(Maori_days())
        break
    else:
        print("Please enter A or B or C")
