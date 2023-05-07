#Make it in to a function
import random
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
Maori_days()
