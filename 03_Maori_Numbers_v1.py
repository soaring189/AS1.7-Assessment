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


#Second choice:
#(It was discarded because there was too much extra code to write)
#random_number = random.randint(1, 10)
#user_answer = input(f"What is number{random_number} in Maori language: ").lower()
#if random_number == 1 and user_answer == "tahi":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 2 and user_answer == "rua":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 3 and user_answer == "toru":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 4 and user_answer == "whā":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 4 and user_answer == "wha":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 5 and user_answer == "tahi":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 6 and user_answer == "rima":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 7 and user_answer == "ono":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 8 and user_answer == "whitu":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 9 and user_answer == "iwa":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#elif random_number == 10 and user_answer == "tekau":
#    print("Correct!")
#    score += 1
#    print(f"Your score is now ({score}/10)")
#else:
#    print("Wrong")
#    print(f"Your score is now ({score}/10)")
