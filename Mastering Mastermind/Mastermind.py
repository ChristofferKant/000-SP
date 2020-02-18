import random
numbers_examples = [0, 1, 2, 3, 4, 5]
numbers = [(i, j, k, l) for i in range(0, 6) for j in range(0, 6) for k in range(0, 6) for l in range(0, 6)] # Lijst met alle mogelijkheden
difficulty_options = ["S", "N", "E"]
secret = random.choice(numbers)		# Secret code voor AI

def main_menu():
	print("""Welcome to Mastermind.				# Intro text
At what difficulty would you like to play?		
Simple means a simple algorithm will try to figure out your code or you will have 10 turns to guess the code.
Normal means an average algorithm will try to figure out your code or you will have 8 turn to guess the code.
Expert means an advanced algorithm will (always) figure out your code or you will have 6 turns to guess the code
Please enter \"S\" for simple, \"N\" for normal or \"E\" for expert)""")

	while True:			# Slaat de moeilijkheidsgraad op
		difficulty = str(input("Enter your choice here: "))
		if difficulty in difficulty_options:
			break
		print("Please enter \"S\", \"N\" or \"E\"")

	print("Who will be entering the code? (ME/AI)")

	while True:			# Slaat op wie de code gaat maken
		code_maker = str(input("Enter your choice here: "))
		if code_maker == "ME":
			player_codemaker(difficulty)
			break
		elif code_maker == "AI":
			ai_codemaker(difficulty)
			break
		print("Please enter \"ME\" or \"AI\"")



def player_codemaker(difficulty):
	print("Choose 4 numbers. You can choose from", numbers_examples)
	number_1 = int(input("Number 1 is: "))
	number_2 = int(input("Number 2 is: "))
	number_3 = int(input("Number 3 is: "))
	number_4 = int(input("Number 4 is: "))
	pass									# Hier komen de algoritmes


def ai_codemaker(difficulty):
	print("""The AI set the code""")
	if difficulty == "S":
		max_turns = 11
	elif difficulty == "N":
		max_turns = 9
	elif difficulty == "E":
		max_turns = 7
	turn = 1
	while turn < max_turns:
		print("Turn", turn)
		number_1 = int(input("Number 1 is: "))
		number_2 = int(input("Number 2 is: "))
		number_3 = int(input("Number 3 is: "))
		number_4 = int(input("Number 4 is: "))
		check(number_1, number_2, number_3, number_4)
		turn += 1
		print(secret)
	print("The secret code is: ", secret)


def check(a, b, c, d):
	guess = (a, b, c, d)
	black_pegs = 0
	white_pegs = 0
	secret_copy = list(secret)
	i = 0
	for n in range(len(guess)):
		if guess[i] == secret[i]:
			black_pegs += 1
			secret_copy.remove(guess[i])
		i += 1
	i = 0
	for n in range(len(secret_copy)):
		if guess[i] in secret_copy:
			white_pegs += 1
			secret_copy.remove(guess[i])
		i += 1
	print("{} black peg(s),{} white peg(s)".format(black_pegs, white_pegs))
	return black_pegs, white_pegs


ai_codemaker("S")