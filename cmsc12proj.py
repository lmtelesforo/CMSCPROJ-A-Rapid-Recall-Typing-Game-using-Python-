import time
import random
import string
import os

def main():
	time.sleep(0.5)
	print()
	print("   \033[0;36m_.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._")
	print(".-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.")	
	print(" )                                                                           (")
	print("""(              \033[0;35m\033[1m█░█░█ █░█ ▄▀█ ▀█▀   █▀▄ █ █▀▄   █   █▀ ▄▀█ █▄█ ▀█\033[0m              \033[0;36m) 
 )           \033[0;35m  ▀▄▀▄▀ █▀█ █▀█ ░█░   █▄▀ █ █▄▀   █   ▄█ █▀█ ░█░ ░▄\033[0m             \033[0;36m(""")
	print("\033[0;36m(                                                                             )")
	print(" )                             \033[1;33m "+".・。.・゜✭・."+"\033[0;36m                               (")
	print("(                                                                             )")
	print(" )                   \033[1;31m\033[5mnote: quick memorization skills required!\033[0m               \033[0;36m(")
	print("(                                                                             )")
	print(" )                                                                           (")
	print("(     \033[0mType the pattern. The more correct answers you get,  the longer the     \033[0;36m)")
	print(" )                        \033[0mpattern gets. Goodluck. :D                         \033[0;36m(")
	print("(                                                                             )")
	print(" )                                  \033[1;33m[1] Easy        \033[0m                     \033[0;36m    (")
	print("(                                \033[1;33m  [2] Medium        \033[0m                    \033[0;36m     )")
	print(" )                    \033[1;33m    [3] Hard (lowercase letters)  \033[0m                 \033[0;36m    (")
	print("(                      \033[1;33m  [4] H3LLf1RE (case-sensitive)   \033[0m              \033[0;36m       )")
	print(" )                           \033[1;33m    [5] Leaderboard        \033[0m              \033[0;36m       (")
	print("(                            \033[1;33m  [6] Developer Mode         \033[0m                  \033[0;36m  )")
	print(" \033[0;36m)                                 \033[1;33m [0] Exit      \033[0m                       \033[0;36m    (")
	print("(                                                                             )")
	print(" )___       _       _       _       _       _       _       _       _     ___(")
	print("    `-._.-' `-._.-' `-._.-' `-._.-' `-._.-' `-._.-' `-._.-' `-._.-' `-._.-'\033[0m")

	print()
	choice = int(input("\033[1;31m》 ◦ Pick your poison: ◦ 《	\033[0m"))

	return choice

def countdown():	
	print("\033[1;33m---------------\033[0m")
	print()
	countdown_str = "Memorize in " 
	for i in range(5, 0, -1):
		i = str(i)
		# countdown_str = countdown_strprev
		countdown_str += i + "... "
		print(countdown_str,end="\r")
		time.sleep(1)

def player_record(score, result, difficulty):
	print()
	print("\033[0;35mSave Player Data for Player Rankings:\033[0m",end="\n")
	name = input("Enter name: \033[1;31m")
	print("\033[0m")

	file = open("player_leaderboard.txt","r")
	if os.path.getsize("player_leaderboard.txt") == 0:
		file = open("player_leaderboard.txt","w")
		score = str(score)
		C
		file.write(name + ",")
		file.write(result + ",")
		file.write(difficulty + ",")
		file.write("rank" + "\n")
		# file.readlines()
		# file.sort()
		file.close()

	else:
		file = open("player_leaderboard.txt","a")
		score = str(score)
		file.write(score + ",")
		file.write(name + ",")
		file.write(result + ",")
		file.write(difficulty + ",")
		file.write("rank" + "\n")
		# file.readlines()
		# file.sort()
		file.close()

	file.close()

	print("\033[0;36m ____________________________________")
	print("|  ________________________________  |")
	print("| |                                | |")
	print("| |   \033[0m\033[0;35m\033[5mHigh Score Data Saved! :D\033[0;36m    | |")
	print("| |                                | |")
	print("      \033[0mName: ", name)
	print("      Score: ", score)
	print("      Last Pattern: ", result)
	print("      Difficulty: ", difficulty,"")
	print("\033[0;36m| |                                | |")	
	print("| |       \033[1;31mCongratulations!       \033[0m \033[0;36m | |")
	print("| |________________________________| |")
	print("|____________________________________|\033[0m")

	while True:
		print()
		play_again = input("\033[0;35mPlay again? [Y/N] \033[0m")
		if play_again == "Y":
			break
		if play_again == "N":
			print()
			print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
			quit()

def easy():
	score = 0
	difficulty = "Easy"
	#  only lowercase English alphabet characters (a-z)
	letters = string.ascii_lowercase
	result = ''.join(random.choice(letters) for i in range(3))
	print()
	print(".・。.・゜✭・.")
	print()
	print("Ready?")
	print()
	time.sleep(0.8)
	print("\033[1;33m---------------\033[0m")
	print("The pattern is:")
	print("\033[0;36m"+result+"\033[0m")
	countdown()
	os.system("cls")
	print("\033[1;31mWhat was the pattern?\033[0m")
	print("\033[1;33mAnswer: \033[0m",end="")
	answer = input()

	if answer == result:
		print()
		print("Nice! Here's a longer one. :D")
		score = 1
		i = 2
		j = 1

		while True:
			add_score = i + j
			letters = string.ascii_lowercase
			result = ''.join(random.choice(letters) for i in range(3+i))
			print()
			print(".・。.・゜✭・.")
			print()
			print("Ready?")
			print()
			time.sleep(0.8)
			print("\033[1;33m---------------\033[0m")
			print("The pattern is:")
			print("\033[0;36m"+result+"\033[0m")
			countdown()
			os.system("cls")
			print("\033[1;31mWhat was the pattern?\033[0m")
			print("\033[1;33mAnswer: \033[0m",end="")
			answer = input()
			i += 1

			if answer != result:
				print("Oof! The pattern was", result, end=".")
				print()
				print("Your score is:", score)
				player_record(score, result, difficulty)
				# score lang dito ay 1 kapag sa first iteration ay mali
				break

			if answer == result:
				print()
				print("Nice! Another one! XD")
				j += 1
				score = score + add_score
				print("Your score is:", score)
				continue

	else:
		print()
		print("Boo! Not even a single point? >:(") 
		while True:
			print()
			play_again = input("\033[0;35mPlay again? [Y/N] \033[0m")
			if play_again == "Y":
				break
			if play_again == "N":
				print()
				print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
				quit()	
		# hindi nakakuha ng isang point, walang place sa leaderboards

def medium():
	score = 0
	difficulty = "Medium"
	letters = string.ascii_lowercase
	numbers = string.digits
	containsDigit = False
	containsLetters = False

	while containsDigit == False and containsLetters == False:
		pattern = ''.join(random.choice(letters + numbers) for i in range(4))
		for char in pattern:
			if char.isdigit():
				containsDigit = True
		if containsDigit == True:
			for char1 in pattern: 
				if char1.islower():
					containsLetters = True
		if containsDigit == True and containsLetters == True:
			result = pattern

	#  only lowercase English alphabet characters (a-z) + numbers (0-9)

	if containsDigit == True and containsLetters == True:
		print()
		print(".・。.・゜✭・.")
		print()
		print("Ready?")
		print()
		time.sleep(0.8)
		print("\033[1;33m---------------\033[0m")
		print("The pattern is:")
		print("\033[0;36m"+result+"\033[0m")
		countdown()
		os.system("cls")
		print("\033[1;31mWhat was the pattern?\033[0m")
		print("\033[1;33mAnswer: \033[0m",end="")
		answer = input()

		if answer == result:
			print()
			print("Nice! Here's a longer one. :D")
			score = 2
			i = 2
			j = 2

			while True:
				add_score = i + j
				letters = string.ascii_lowercase
				numbers = string.digits
				containsDigit = False
				containsLetters = False

				while containsDigit == False and containsLetters == False:
					pattern = ''.join(random.choice(letters + numbers) for i in range(4+i))
					for char in pattern:
						if char.isdigit():
							containsDigit = True
					if containsDigit == True:
						for char1 in pattern: 
							if char1.islower():
								containsLetters = True
					if containsDigit == True and containsLetters == True:
						result = pattern

				if containsDigit == True and containsLetters == True:
					print()
					print(".・。.・゜✭・.")
					print()
					print("Ready?")
					print()
					time.sleep(0.8)
					print("\033[1;33m---------------\033[0m")
					print("The pattern is:")
					print("\033[0;36m"+result+"\033[0m")
					countdown()
					os.system("cls")
					print("\033[1;31mWhat was the pattern?\033[0m")
					print("\033[1;33mAnswer: \033[0m",end="")
					answer = input()
					i += 2

					if answer != result:
						print("Oof! The pattern was", result, end=".")
						print()
						print("Your score is:", score)
						player_record(score, result,difficulty)
						# score lang dito ay 1 kapag sa first iteration ay mali
						break

					if answer == result:
						print()
						print("Nice! Another one! XD")	
						j += 2
						score = score + add_score
						print("Your score is:", score)
						continue

		else:
			print()
			print("Boo! Not even a single point? >:(")  
			while True:
				print()
				play_again = input("\033[0;35mPlay again? [Y/N] \033[0m")
				if play_again == "Y":
					break
				if play_again == "N":
					print()
					print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
					quit()	

def hard():
	# not case-sensitive
	score = 0
	difficulty = "Hard"
	letters = string.ascii_lowercase
	numbers = string.digits
	nonalpha = string.punctuation
	containsDigit = False
	containsLetters = False
	containsPunct = False

	while True:
		pattern = ''.join(random.choice(letters + numbers + nonalpha) for i in range(5))
		for char in pattern:
			if char.isdigit():
				containsDigit = True
			if char.islower():
				containsLetters = True
			if char in string.punctuation:
				containsPunct = True

	#  only lowercase English alphabet characters (a-z) + numbers (0-9) + nonalpha
	
		if containsDigit == True and containsPunct == True and containsLetters == True:
			result = pattern
			break
		else:
			continue

	if containsDigit == True and containsLetters == True and containsPunct == True:
		print()
		print(".・。.・゜✭・.")
		print()
		print("Ready?")
		print()
		time.sleep(0.8)
		print("\033[1;33m---------------\033[0m")
		print("The pattern is:")
		print("\033[0;36m"+result+"\033[0m")
		countdown()
		os.system("cls")
		print("\033[1;31mWhat was the pattern?\033[0m")
		print("\033[1;33mAnswer: \033[0m",end="")
		answer = input()

		if answer == result:
			print()
			print("Nice! Here's a longer one. :D")
			score = 3
			i = 2
			j = 2
			while True:
				add_score = i + j
				letters = string.ascii_lowercase
				numbers = string.digits
				containsDigit = False
				containsLetters = False
				containsPunct = False

				while True:
					pattern = ''.join(random.choice(letters + numbers + nonalpha) for i in range(5+i))
					for char in pattern:
						if char.isdigit():
							containsDigit = True
						if char.islower():
							containsLetters = True
						if char in string.punctuation:
							containsPunct = True
					if containsDigit == True and containsPunct == True and containsLetters == True:
						result = pattern
						break
					else:
						continue

				if containsDigit == True and containsPunct == True and containsLetters == True:
					print()
					print(".・。.・゜✭・.")
					print()
					print("Ready?")
					print()
					time.sleep(0.8)
					print("\033[1;33m---------------\033[0m")
					print("The pattern is:")
					print("\033[0;36m"+result+"\033[0m")
					countdown()
					os.system("cls")
					print("\033[1;31mWhat was the pattern?\033[0m")
					print("\033[1;33mAnswer: \033[0m",end="")
					answer = input()
					i += 2

					if answer != result:
						print("Oof! The pattern was", result, end=".")
						print()
						print("Your score is:", score)
						player_record(score, result,difficulty)
						break

					if answer == result:
						print()
						print("Nice! Another one! XD")	
						j += 3
						score = score + add_score
						print("Your score is:", score)
						continue

		else:
				print("Boo! Not even a single point? >:(")  
				while True:
					print()
					play_again = input("\033[0;35mPlay again? [Y/N] \033[0m")
					if play_again == "Y":
						break
					if play_again == "N":
						print()
						print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
						quit()	

def hellfire():
	score = 0
	difficulty = "Hellfire"
	lower_letters = string.ascii_lowercase
	upper_letters = string.ascii_uppercase
	numbers = string.digits
	nonalpha = string.punctuation
	containsDigit = False
	containsPunct = False
	containsLetters = False
	containsULetters = False

	while True:
		pattern = ''.join(random.choice(lower_letters + upper_letters + numbers + nonalpha) for i in range(6))
		
		for char in pattern:
			if char.isdigit():
				containsDigit = True
			if char.islower():
				containsLetters = True
			if char in string.punctuation:
				containsPunct = True
			if char.isupper():
				containsULetters = True
	
		if containsDigit == True and containsPunct == True and containsLetters == True and containsULetters == True:
			result = pattern
			break
		else:
			continue

	#  only lowercase English alphabet characters (a-z) + numbers (0-9) + nonalpha + case-sensitive

	if containsDigit == True and containsPunct == True and containsLetters == True and containsULetters == True:
		print()
		print(".・。.・゜✭・.")
		print()
		print("Ready?")
		print()
		time.sleep(0.8)
		print("\033[1;33m---------------\033[0m")
		print("The pattern is:")
		print("\033[0;36m"+result+"\033[0m")
		countdown()
		os.system("cls")
		print("\033[1;31mWhat was the pattern?\033[0m")
		print("\033[1;33mAnswer: \033[0m",end="")
		answer = input()

		if answer == result:
			print()
			print("Nice! Here's a longer one. :D")
			score = 4
			i = 3
			j = 3

			while True:
				add_score = i + j
				lower_letters = string.ascii_lowercase
				upper_letters = string.ascii_uppercase
				numbers = string.digits
				containsDigit = False
				containsLetters = False
				containsPunct = False
				containsULetters = False

				while True:
					pattern = ''.join(random.choice(lower_letters + upper_letters + numbers + nonalpha) for i in range(6+i))
					
					for char in pattern:
						if char.isdigit():
							containsDigit = True
						if char.islower():
							containsLetters = True
						if char in string.punctuation:
							containsPunct = True
						if char.isupper():
							containsULetters = True

					if containsDigit == True and containsPunct == True and containsLetters == True and containsULetters == True:
						result = pattern
						break
					else:
						continue

				if containsDigit == True and containsULetters == True and containsPunct == True and containsLetters == True:
					print()
					print(".・。.・゜✭・.")
					print()
					print("Ready?")
					print()
					time.sleep(0.8)
					print("\033[1;33m---------------\033[0m")
					print("The pattern is:")
					print("\033[0;36m"+result+"\033[0m")
					countdown()
					os.system("cls")
					print("\033[1;31mWhat was the pattern?\033[0m")
					print("\033[1;33mAnswer: \033[0m",end="")
					answer = input()
					i += 2

					if answer != result:
						print("Oof! The pattern was", result, end=".")
						print()
						print("Your score is:", score)
						player_record(score, result,difficulty)
						break

					if answer == result:
						print()
						print("Nice! Another one! XD")	
						j += 3
						score = score + add_score
						print("Your score is:", score)
						continue

		else:
			print("Boo! Not even a single point? >:(")  
			while True:
				print()
				play_again = input("\033[0;35mPlay again? [Y/N] \033[0m")
				if play_again == "Y":
					break
				if play_again == "N":
					print()
					print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
					quit()	

def leaderboards():
	file = open("player_leaderboard.txt","r")
	leaderboard = []
	sort = []
	for line in file.readlines():
		entry = line[:-1].split(",")
		leaderboard.append(entry)
	for i in range(len(leaderboard)):
		name = leaderboard[i][1]
		score = leaderboard[i][0]
		pattern = leaderboard[i][2]
		mode = leaderboard[i][3]
		rank = leaderboard[i][4]
	file.close()

	print()
	print("     \033[0;36m________________________________________________________")
	print("    /",end="")
	print("\\",end="                                                      ")                                                   
	print("\\")
	print("(O)===)------------------------------------------------------)==(O)")
	print("    \\",end="")
	print("/",end="                                                      ")                                                   
	print("/\033[0m")
	print("""
            \033[0;35m\033[1m█░░ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█ █▄▄ █▀█ ▄▀█ █▀█ █▀▄\033[0m   
            \033[0;35m█▄▄ ██▄ █▀█ █▄▀ ██▄ █▀▄ █▄█ █▄█ █▀█ █▀▄ █▄▀\033[0m""")
	print()
	print("\033[1;33m "+"                        .・。.・゜✭・."+"\033[0;36m ")
	print()
	print("       ",end="")
	print("\033[0;31mRank",end="  ")
	print("Name",end="   ")
	print("   Score",end=" ")
	print(" Last Pattern",end="  ")
	print("     Mode\033[0m")

	for rank in range(0,len(leaderboard)):
		leaderboard[rank][0] = int(leaderboard[rank][0])

	leaderboard.sort(reverse=True)
	rank = 1

	for place in range(0,len(leaderboard)):
		rank1 = str(rank)
		leaderboard[place][4] = str(leaderboard[place][2])
		leaderboard[place][2] = str(leaderboard[place][0])
		leaderboard[place][2] = str(leaderboard[place][3])
		leaderboard[place][3] = str(leaderboard[place][4])
		leaderboard[place][4] = str(leaderboard[place][2])
		leaderboard[place][2] = str(leaderboard[place][0])
		leaderboard[place][0] = str(rank1)
		rank += 1
	columns = 5

	for place in range(0,len(leaderboard)):
		for first, second, third, fourth, fifth in zip(leaderboard[place][::columns], leaderboard[place][1::columns], leaderboard[place][2::columns], leaderboard[place][3::columns], leaderboard[place][4::columns]):
		    print(f'         {first: <4}{second: <11}{third: <6}{fourth: <19}{fifth}')    

	print()
	print()
	print("     \033[0;36m----------8<---------------[ congratulations! ]---------\033[0m")

	print()
	while True:
		prompt = input("Back to Main Menu? Choosing No would end the game. [Y/N] ")
		if prompt == "Y":
			print(end="")
			break
		if prompt == "N":
			print()
			print("\033[1;33mThanks for playing! Goodbye! :D\033[0m")
			quit()	
		else:
			continue


def dev_leaderboard():
	file = open("player_leaderboard.txt","r")
	leaderboard = []
	sort = []
	for line in file.readlines():
		entry = line[:-1].split(",")
		leaderboard.append(entry)
	for i in range(len(leaderboard)):
		name = leaderboard[i][1]
		score = leaderboard[i][0]
		pattern = leaderboard[i][2]
		mode = leaderboard[i][3]
		rank = leaderboard[i][4]
	file.close()

	print()
	print("     \033[0;36m________________________________________________________")
	print("    /",end="")
	print("\\",end="                                                      ")                                                   
	print("\\")
	print("(O)===)------------------------------------------------------)==(O)")
	print("    \\",end="")
	print("/",end="                                                      ")                                                   
	print("/\033[0m")
	print("""
            \033[0;35m\033[1m█░░ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█ █▄▄ █▀█ ▄▀█ █▀█ █▀▄\033[0m   
            \033[0;35m█▄▄ ██▄ █▀█ █▄▀ ██▄ █▀▄ █▄█ █▄█ █▀█ █▀▄ █▄▀\033[0m""")
	print()
	print("\033[1;33m "+"                        .・。.・゜✭・."+"\033[0;36m ")
	print()
	print("       ",end="")
	print("\033[0;31mRank",end="  ")
	print("Name",end="   ")
	print("   Score",end=" ")
	print(" Last Pattern",end="  ")
	print("     Mode\033[0m")

	for rank in range(0,len(leaderboard)):
		leaderboard[rank][0] = int(leaderboard[rank][0])

	leaderboard.sort(reverse=True)
	rank = 1
	for place in range(0,len(leaderboard)):
		rank1 = str(rank)
		leaderboard[place][4] = str(leaderboard[place][2])
		leaderboard[place][2] = str(leaderboard[place][0])
		leaderboard[place][2] = str(leaderboard[place][3])
		leaderboard[place][3] = str(leaderboard[place][4])
		leaderboard[place][4] = str(leaderboard[place][2])
		leaderboard[place][2] = str(leaderboard[place][0])
		leaderboard[place][0] = str(rank1)
		rank += 1
	columns = 5

	for place in range(0,len(leaderboard)):
		for first, second, third, fourth, fifth in zip(leaderboard[place][::columns], leaderboard[place][1::columns], leaderboard[place][2::columns], leaderboard[place][3::columns], leaderboard[place][4::columns]):
		    print(f'         {first: <4}{second: <11}{third: <6}{fourth: <19}{fifth}')    

	print()
	print()
	print("     \033[0;36m----------8<---------------[ developer mode ]---------\033[0m")

def delete_player():
	choice = input("Delete a player data? [Y/N] ")
	if choice == "Y":
		print()
		player_data_rank = input("Input Player Rank: ")

		file = open("player_leaderboard.txt","r")
		leaderboard = []
		dictionary = {}
		for line in file.readlines():
			entry = line[:-1].split(",")
			leaderboard.append(entry)
		for i in range(len(leaderboard)):
			name = leaderboard[i][1]
			# keys.append(name)
			score = leaderboard[i][0]
			pattern = leaderboard[i][2]
			mode = leaderboard[i][3]
			rank = leaderboard[i][4]
		file.close()

		for rank in range(0,len(leaderboard)):
			leaderboard[rank][0] = int(leaderboard[rank][0])
		leaderboard.sort(reverse=True)

		rank = 1
		for place in range(0,len(leaderboard)):
			rank1 = str(rank)
			leaderboard[place][4] = str(leaderboard[place][2])
			leaderboard[place][2] = str(leaderboard[place][0])
			leaderboard[place][2] = str(leaderboard[place][3])
			leaderboard[place][3] = str(leaderboard[place][4])
			leaderboard[place][4] = str(leaderboard[place][2])
			leaderboard[place][2] = str(leaderboard[place][0])
			leaderboard[place][0] = str(rank1)
			Rank = leaderboard[place][0]
			Name = leaderboard[place][1]
			Score = leaderboard[place][2]
			LastPattern = leaderboard[place][3]

			dictionary[Rank] = [Name,Score,LastPattern]
			rank += 1

		if player_data_rank in dictionary.keys():
			print()
			placeholder = dictionary[player_data_rank][0]
			last_pattern = dictionary[player_data_rank][2]

			while True:
				option = input("Are you sure you want to delete Player "+placeholder+"? [Y/N] ")
				if option == "Y":
					Rank = player_data_rank
					dictionary.pop(player_data_rank)

					file = open("player_leaderboard.txt","r")
					lines = file.readlines()
					file = open("player_leaderboard.txt","w")
					for line in lines:
						if line.find(last_pattern) == -1:
							file.write(line)
					file.close()
					print()
					print("Bye bye, player", placeholder,end="! :(")
					print()
					dev_leaderboard()
					print()
					break
				if option == "N":
					print("Well, okay then!")
					print()
					break
				else:
					print("Invalid input.")
					continue

		else:
			print()
			print("Player not found. Try again.")
			print()

	if choice == "N":
		print("\n? Why are you here then?")
		print()

	else: 
		delete_player()

def add_player():
	choice = input("Add a player data? [Y/N] ")
	if choice == "Y":
		print()
		player_data_name = input("Input Player Name: ")
		player_data_score = input("Input Player Score: ")
		player_data_lastp = input("Input Player's Last Pattern: ")
		player_data_mode = input("Input Player's Game Difficulty: ")

		file = open("player_leaderboard.txt","a")
		leaderboard = []
		file = open("player_leaderboard.txt","a")
		file.write(player_data_score + ",")
		file.write(player_data_name + ",")
		file.write(player_data_lastp + ",")
		file.write(player_data_mode + ",")
		file.write("rank" + "\n")
		file.close()

		for rank in range(0,len(leaderboard)):
			leaderboard[rank][0] = int(leaderboard[rank][0])
		leaderboard.sort(reverse=True)

		rank = 1
		for place in range(0,len(leaderboard)):
			rank1 = str(rank)
			leaderboard[place][4] = str(leaderboard[place][2])
			leaderboard[place][2] = str(leaderboard[place][0])
			leaderboard[place][2] = str(leaderboard[place][3])
			leaderboard[place][3] = str(leaderboard[place][4])
			leaderboard[place][4] = str(leaderboard[place][2])
			leaderboard[place][2] = str(leaderboard[place][0])
			leaderboard[place][0] = str(rank1)
			Rank = leaderboard[place][0]
			Name = leaderboard[place][1]
			Score = leaderboard[place][2]
			rank += 1

		print()
		print(player_data_name,"added to leaderboard. :)")
		dev_leaderboard()
		print()

	if choice == "N":
		print("\n? Why are you here then?")
		print()

	else:
		add_player()

def dev_mainmenu():
	print("---------------------------------------")
	print("""[1] Add Player Data to Leaderboard
[2] Delete Player Data from Leaderboard
[3] Exit Developer Mode""")
	print("---------------------------------------")
	print()
	opt_add_del = int(input("Input Choice: "))
	print()
	if opt_add_del == 1:
		add_player()
	if opt_add_del == 2:
		delete_player()
	if opt_add_del == 3:
		time.sleep(0.5)
		print("Exiting Developer Mode...")
		time.sleep(0.9)
		print("Thanks, Dev Laira! Goodbye! :D")
		# bakit minsan nabalik sya sa dev main menu? check kung maayos yung pagbabalik ng main
	else:
		dev_mainmenu()

def devmode():
	print()
	time.sleep(0.8)
	print("Initializing Developer Mode...")
	time.sleep(0.8)
	password = input("Input Password: ")

	if password == "lairaxx":
		print()
		print("Hello, Dev Laira!")
		print("Welcome to Developer Mode. (ﾉ≧∇≦)ﾉ ﾐ ┸━┸")
		dev_leaderboard()
		print()
		dev_mainmenu()

	else:
		print()
		print("Wrong password. Hands off, players! (╯ರ ~ ರ）╯︵ ┻━┻")

print()
import loading

while True:
	choice = main()

	if choice == 1:
		easy()

	if choice == 2:
		medium()

	if choice == 3:
		hard()

	if choice == 4:
		hellfire()

	if choice == 5:
		leaderboards()

	if choice == 6:
		devmode()

	if choice == 0:
		print()
		print("\033[1;31mThanks for playing! Goodbye! :D\033[0m",end="")
		import thanks
		exit()