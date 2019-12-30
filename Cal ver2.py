a = int(input("enter First number: "))
c = input("enter Calculate Sign: ")
b = int(input("enter Second number: "))

if c == "+":
	result = a + b
	print (a, "+" ,b, "=", result)

elif c == "-":
	result = a - b
	print (a, "-" ,b, "=", result)

elif c == "*":
	result = a * b
	print (a, "*" ,b, "=", result)

elif c == "/":
	result = a / b
	print (a, "/" ,b, "=", result)

elif c == "**":
	result = a ** b
	print (a, "**" ,b, "=", result)


else:
	print("You enter WRONG Calculate Sign")

