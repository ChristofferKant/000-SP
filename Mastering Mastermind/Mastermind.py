import random
colors = ["[R]ed", "[G]reen", "[B]lue", "[Y]ellow", "[P]urple", "[W]hite"]

def main_menu():
	print("""Welcome to Mastermind.
Who will be making the code? (ME/AI)""")

	while True:
		code_maker = str(input("Enter your choice here: "))
		if code_maker == "ME":
			player_codemaker()
			continue
		elif code_maker == "AI":
			ai_codemaker()
			continue
		print("Please enter \"ME\" or \"AI\"")


def player_codemaker():
	while True:
		print("""At what difficulty would you like to play?
You can choose between simple, normal or expert. (S/N/E)
Simple means a simple algorithm will try to figure out your code.
Normal means an average algorithm will try to figure out your code.
Expert means an advanced algorithm will figure out your code.""")
		difficulty = str(input("Enter your choice here: "))
		if difficulty == "S" or "N" or "E":
			break
		print("Please enter \"S\", \"N\" or \"E\"")

	print("""Choose 4 colors.
You can choose from """, colors)
	color_1 = str(input("Color 1 is: "))
	color_2 = str(input("Color 2 is: "))
	color_3 = str(input("Color 3 is: "))
	color_4 = str(input("Color 4 is: "))

	possible_combinations = []

def ai_codemaker():
	while True:
		print("""At what difficulty would you like to play?
You can choose between simple, normal or expert. (S/N/E)
Simple means you have 10 turns to guess the code.
Normal means you have 8 turns to guess the code.
Expert means you have 6 turns to guess the code.""")
		difficulty = str(input("Enter your choice here: "))
		if difficulty == "S" or "N" or "E":
			break
		print("Please enter \"S\", \"N\" or \"E\"")
	pass


player_codemaker()