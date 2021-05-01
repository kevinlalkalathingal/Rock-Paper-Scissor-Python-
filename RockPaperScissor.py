import random 
import math
	
name = input("Enter your name:")
user_score = 0
comp_score = 0
while True:
	print("Enter your choice:\n1.rock\n2.paper\n3.scissor\n")
	user_input = int(input("Enter your choice:"))
	
	if user_input > 3 or user_input < 1:
		user_input = int(input("Enter Valid input:"))

	if user_input == 1:
		user_choice = "rock"
	elif user_input == 2:
		user_choice = "paper"
	elif user_input == 3:
		user_choice = "scissor"
	
	comp_input = random.randrange(1, 3)
	
	while comp_input == user_input:
		comp_input = random.randint(1, 3)
	
	if comp_input == 1:
		comp_choice = "rock"
	elif comp_input == 2:
		comp_choice = "paper"
	elif comp_input == 3:
		comp_choice = "scissor"
	
	print("Computer has chosen " + comp_choice)
	
	if user_input == comp_input:
		print("TIE")
	elif user_input == 1 and comp_input == 2:
		print(user_choice + " V/S " + comp_choice)
		print("Computer Wins")
		comp_score += 1
	elif user_input == 1 and comp_input == 3:
		print(user_choice + " V/S " + comp_choice)
		print("You Win")
		user_score += 1
	elif user_input == 2 and comp_input == 1:
		print(user_choice + " V/S " + comp_choice)
		print("You Win")
		user_score += 1
	elif user_input == 2 and comp_input == 3:
		print(user_choice + " V/S " + comp_choice)
		print("Computer Wins")
		comp_score += 1
	elif user_input == 3 and comp_input == 1:
		print(user_choice + " V/S " + comp_choice)
		print("Computer Wins")
		comp_score += 1
	elif user_input == 3 and comp_input == 2:
		print(user_choice + " V/S " + comp_choice)
		print("You Win")
		user_score += 1
			
	print("Try Again?(Y/N)")
	ans = input()
	if ans == 'n' or ans == 'N':
		print("Thank you for playing")
		print("\tTotal Score\n" + str(name) + "\t\tComputer\n" , int(user_score), "\t\t", int(comp_score))
		if user_score > comp_score:
			print("Congratulations!")
		else:
			print("Better Luck Next Time ;)")
		print("\nPress (n/N) again to exit")
		ans2 = input()
		if ans == 'n' or ans == 'N':
			break
		