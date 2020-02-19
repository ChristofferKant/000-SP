# https://www.edureka.co/community/16988/python-exit-commands-why-so-many-and-when-should-each-be-used voor sys.exit()
# https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating voor lst[:]
# programmeursleerling bladzijde 166 (180 in pdf) voor numbers lijst (regel 7)
import random
import sys
numbers = [(i, j, k, l) for i in range(0, 6) for j in range(0, 6) for k in range(0, 6) for l in range(0, 6)] # Lijst met alle mogelijkheden
secret = random.choice(numbers)		# Secret code voor AI


def main_menu():
	difficulty_options = ["S", "N", "E"]
	code_maker_options = ["ME", "AI"]

	print("""Welcome to Mastermind.			
At what difficulty would you like to play?		
Enter \"S\" for simple, \"N\" for normal or \"E\" for expert.
Enter \"R\" for the rules.""")

	difficulty = str(input("Enter your choice here: "))
	while difficulty not in difficulty_options:  				# Slaat de moeilijkheidsgraad op
		if difficulty == "R":
			rules()
		print("Please enter \"S\", \"N\", \"E\" or \"R\"")
		difficulty = str(input("Enter your choice here: "))

	print("Who will be making the secret code? (ME/AI)")
	code_maker = str(input("Enter your choice here: "))
	if code_maker == "ME":
		player_codemaker(difficulty)
	elif code_maker == "AI":
		ai_codemaker(difficulty)
	while code_maker not in code_maker_options:
		if code_maker == "ME":
			player_codemaker(difficulty)
		elif code_maker == "AI":
			ai_codemaker(difficulty)
		print("Please enter \"ME\" or \"AI\"")
		code_maker = str(input("Enter your choice here: "))


def rules():
	print("""The rules of Mastermind:
The object of Mastermind is to guess the hidden code.
After you take a guess you will get feedback as either black pegs or white pegs.
Black pegs indicate the number and the position is correct.
White pegs indicate just the number is correct, but the position is not. 
You win Mastermind if you get 4 black pegs within the turn limit.
As for difficulty settings:
- Simple means a simple algorithm will try to figure out your code or you will have 10 turns to guess the code.
- Normal means an average algorithm will try to figure out your code or you will have 8 turn to guess the code.
- Expert means an advanced algorithm will (always) figure out your code or you will have 6 turns to guess the code.""")
	main_menu()


def player_codemaker(difficulty):
	secret = insert_code()
	print("The code is set.")
	print("secret is ", secret)
	max_turns = 10

	for turn in range(1, max_turns + 1):
		print("Turn", turn)
		if difficulty == "S":
			ai_guess = ai_simple_guess(turn)
			print("AI Guess is ", ai_guess)
			feedback = check_secret(ai_guess, secret)
			print("Feedback response is", feedback)
			filter_list(ai_guess, feedback, numbers)
			if feedback == (4, 0):
				print("AI has won")
				play_again()
			input(str("Go to next turn? Enter any key"))

		elif difficulty == "N":
			ai_guess = ai_normal_guess(turn)
			print("AI guess is ", ai_guess)
			feedback = check_secret(ai_guess)
			print("Feedback response is", feedback)
			filter_list(ai_guess, feedback, numbers)
			if feedback == (4, 0):
				print("AI has won")
				play_again()
			input(str("Go to next turn? Enter any key"))

		elif difficulty == "E":
			print("Apoligies, this mode is not playable yet.")
			play_again()
	print("AI has run out of turns, you win!")
	play_again()


def insert_code():
	numbers_examples = [0, 1, 2, 3, 4, 5]
	print("Choose 4 numbers to set as secret code. You can choose from", numbers_examples)
	number_1 = int(input("Number 1 is: "))
	number_2 = int(input("Number 2 is: "))
	number_3 = int(input("Number 3 is: "))
	number_4 = int(input("Number 4 is: "))
	inserted_secret = [number_1, number_2, number_3, number_4]
	return inserted_secret


def filter_list(guess, feedback, lst):
	for number in lst[:]:
		check_check = check_guess(number, guess)
		if check_check == feedback:
			continue
		else:
			lst.remove(number)


def ai_simple_guess(turn):	# simple strategy
	if turn == 1:
		first_guess = random.choice(numbers)
		return first_guess
	other_guess = random.choice(numbers)
	return other_guess


def ai_normal_guess(turn):
	if turn == 1:
		first_guess = [0, 0, 1, 1]
		return first_guess
	other_guess = random.choice(numbers)
	return other_guess


def check_guess(number, guess):
	black_pegs = 0
	white_pegs = 0
	guess_copy = list(guess)
	i = 0
	for n in range(len(number)):		# telt de black pegs in de guess
		if number[i] == guess[i]:
			black_pegs += 1
			guess_copy.remove(number[i])
		i += 1
	i = 0
	for n in range(len(guess_copy)):	# telt de white pegs in de guess
		if number[i] in guess_copy:
			white_pegs += 1
			guess_copy.remove(number[i])
		i += 1
	return black_pegs, white_pegs


def check_secret(guess, secret):
	black_pegs = 0
	white_pegs = 0
	secret_copy = list(secret)
	i = 0
	for n in range(len(guess)):				# telt de black pegs
		if guess[i] == secret[i]:
			black_pegs += 1
			secret_copy.remove(guess[i])
		i += 1
	i = 0
	for n in range(len(secret_copy)):		# telt de white pegs
		if guess[i] in secret_copy:
			white_pegs += 1
			secret_copy.remove(guess[i])
		i += 1
	print("{} black peg(s),{} white peg(s).".format(black_pegs, white_pegs))
	return black_pegs, white_pegs


def ai_codemaker(difficulty):
	print("""The AI set the code""")
	if difficulty == "S":			# 10 beurten voor simple
		max_turns = 10
	elif difficulty == "N":			# 8 beurten voor normal
		max_turns = 8
	elif difficulty == "E":			# 6 beurten voor expert
		max_turns = 6

	for turn in range(max_turns + 1):
		print("Turn", turn + 1)
		checked_answer = check_secret(player_guess(), secret)
		print(secret)
		if checked_answer == (4, 0):
			print("Congrats, you are the mastermind!")
			play_again()
		if turn == max_turns:
			print("You ran out of turns, you lose.")
			play_again()
		continue

	print("The secret code is: ", secret)


def player_guess():
	numbers_examples = [0, 1, 2, 3, 4, 5]
	while True:
		number_1 = int(input("Number 1 is: "))
		number_2 = int(input("Number 2 is: "))
		number_3 = int(input("Number 3 is: "))
		number_4 = int(input("Number 4 is: "))
		guess = (number_1, number_2, number_3, number_4)
		if guess not in numbers:
			print("Please enter 4 valid numbers. Every number needs to be one of the following:", numbers_examples)
			continue
		break
	return guess


def play_again():
	print("Would you like to play again?")
	back_to_start = input(str("Enter yes or no (Y/N)."))
	if back_to_start == "Y":
		main_menu()
	elif back_to_start == "N":
		sys.exit()
	else:
		print("Please enter \"Y\" or \"N\".")


main_menu()