#Loops for 10 times
import random
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
