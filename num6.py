num = int(input("input the number(1~9): "))

if num != 0:
	
	for j in range(num,10,1):

		for i in range(1,10):
			result = num * i
			print(num," * ",i, "=" ,result)
		num = num + 1
		print("")

else:
	print("End thr program.")

