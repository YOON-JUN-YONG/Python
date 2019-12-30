import random

def isNumber(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

base = range(1,10)

random_num = random.sample(base,3)

Contin = 0

while True:

	Count = 0

	Strike = 0

	Ball = 0
	
	if Contin == 'yes':	
		base = range(1,10)

		random_num = random.sample(base,3)

		Contin = 0

	Contin = 0

	print("please input 'Three Number'")

	while True:

		num = str(input())
			
		if isNumber(num) == True:
			break
		
		else:
			print("Please input 'THE NUMBER'")
			continue

	if num == '0':
		break

	print("You input",num)

	for i in range(3):
		for j in range(3):
			
			if num[i] == str(random_num[j]) and i == j:
				Strike = Strike +1
			
			if num[i] == str(random_num[j]) and i != j:
				Ball = Ball +1

	print("Strikr: ",Strike,"\tBall: ",Ball)
	print()

	Count = Count +1

	if Strike == 3:
		print("Congratulation!")
		print("You input right number in " ,Count)
		print("The correct answer is ",random_num)

		while True:

			Contin = input("Do you want one more game (Yes/no)")
			Contin.lower()
		
			if Contin == 'yes':
				break

			if Contin == 'no':
				break

			else:
				print("You enter Wrong word")

	if Contin == 'no':
		print("End the Game")
		break

















		
	

