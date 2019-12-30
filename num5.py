import random

random_num = random.randrange(1,101)

num = 0

Count = 0

while num != random_num:

	num = int(input("Input Number (1~100): "))

	if num < random_num:
		print("Number is so low")
	
	elif num > random_num:
		print("Number is so high")

	Count = Count +1
	
else:
	print("Congratulation!")
	print("You input right number in " ,Count)
	print("The correct answer is ",random_num)
