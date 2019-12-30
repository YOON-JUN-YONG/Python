a = int(input("Please enter Number: "))

if 1<a<10 :

	print("#", a, "Time Table#")

	for i in range(1,10):
		result = a * i
		print(a," * ",i, "=" ,result)

else:
	print("You enter WRONG Calculate Sign")
	print("Please enter 2~9 number and restart this program")

