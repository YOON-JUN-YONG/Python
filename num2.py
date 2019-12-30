birth = int(input("please input your birth year: "))

age = 2017 - birth + 1

if 20 <= age <= 26:
	student = 'University'
	print(student+ " Student")

elif 17 <= age < 20:
	student = 'High School'
	print(student+ " Student")

elif 14 <= age < 17:
	student = 'Junior High School'
	print(student+ " Student")

elif 8 <= age < 14:
	student = 'Child'
	print(student)

else:
	print("NOT Student")

