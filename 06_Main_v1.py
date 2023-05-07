#Integrate all functions
import random


def NameAgeChecker():
    while True:
        name = input("Please input your name: ")
        age = input("Please input your age: ")
        confirm = input(f"Name: {name}. Age: {age}. Please enter Yes/No: ").upper()
        if confirm == "Y" or confirm == "YES":
            break


def If_played_before():
    played_before = input("Have you played before?(Y/N)").upper()
    if played_before == "Y" or played_before == "YES":
        pass
    else:
        Say_rules()


def Say_rules():
    print("Welcome to Māori language quiz\n"
          "There are three tests:\n"
          "A:Maori numbers test\n"
          "B:Maori months test\n"
          "C:Maori days test\n"
          "There are ten questions for each test, and you get one point for each correct answer. See how many points you'll get.")


def Maori_numbers():
    score = 0
    for i in range(1, 11):
        random_number = random.randint(1, 10)
        user_answer = input(f"What is number{random_number} in Maori language: ").lower()
        number_list = ["tahi", "rua", "toru", "whā", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
        if user_answer == number_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        elif random_number == 4 and user_answer == "wha":
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)")


def Maori_months():
    score = 0
    for i in range(1, 11):
        random_number = random.randint(1, 12)
        user_answer = input(f"What is the {random_number}th month in Maori language: ").lower()
        month_list = ["hānuere", "hui tanguru", "poutū", "aperira", "me", "pipiri", "hōngongoi", "awatea", "mahuru", "whiringa-ā-rangi", "whiringa ā-rangi", "haki"]
        month_list1 = ["hanuere", "hui tanguru", "poutu", "aperira", "me", "pipiri", "hongongoi", "awatea", "mahuru", "whiringa-a-rangi", "whiringa a-rangi", "haki"]
        if user_answer == month_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        elif user_answer == month_list1[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)")


def Maori_days():
    score = 0
    for i in range(1, 11):
        random_number = random.randint(1, 7)
        user_answer = input(f"What is the {random_number}th day in the week in Maori language: ").lower()
        day_list = ["mane", "tūrei", "te wenerei", "tāite", "paraire", "hātarei", "rātapu"]
        day_list1 = ["mane", "turei", "te wenerei", "taite", "paraire", "hatarei", "ratapu"]
        if user_answer == day_list[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        elif user_answer == day_list1[random_number-1]:
            print("Correct!")
            score += 1
            print(f"Your score is now ({score}/10)")
        else:
            print("Wrong")
            print(f"Your score is now ({score}/10)")


NameAgeChecker()
If_played_before()
while True:
    choose_test = input("Which test do you want to choose(A/B/C): ").upper()
    if choose_test == "A":
        Maori_numbers()
        break
    elif choose_test == "B":
        Maori_months()
        break
    elif choose_test == "C":
        Maori_days()
        break
    else:
        print("Please enter A or B or C")
