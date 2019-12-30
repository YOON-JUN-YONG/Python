first = int(input("please input first number: "))

additional = int(input("please input additional number: "))

result = first * additional

print("Print " ,result, " Table")

for i in range(1,10):
		result2 = result * i
		print(result2," * ",i, "=" ,result2)

