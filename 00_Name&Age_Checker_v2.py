#Make it into a function
def NameAgeChecker():
    while True:
        name = input("Please input your name: ")
        age = input("Please input your age: ")
        confirm = input(f"Name: {name}. Age: {age}. Please enter Yes/No: ").upper()
        if confirm == "Y" or confirm == "YES":
            print(f"Name: {name}. Age: {age}.")
            break
NameAgeChecker()
