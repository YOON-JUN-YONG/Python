Score = int(input("please enter your score: "))

if Score >= 90:
	grade = 'A'

elif Score >= 80:
	grade = 'B'

elif Score >= 70:
	grade = 'C'

elif Score >= 60:
	grade = 'D'

else:
	grade = 'F'

print("Your grade is " +grade)


