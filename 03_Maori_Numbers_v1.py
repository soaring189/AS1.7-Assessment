#Test your Maori language of numbers
import random
score = 0
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
