#Make it in to a function
def If_played_before():
    played_before = input("Have you played before?(Y/N)").upper()
    if played_before == "Y" or played_before == "YES":
        print("Played Before")
    else:
        print("Welcome to Māori language quiz, the rules is ......")
If_played_before()
