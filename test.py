import sys

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print("Calculator machine")
print("If you press 'Enter', You can exit")

while True:

    Cal = str(input())

    if Cal[1] == "+":
        a = int(Cal[0])
        b = int(Cal[2])
        result = add(a,b)
        print(result)

    if Cal[1] == "-":
        a = int(Cal[0])
        b = int(Cal[2])
        result = sub(a,b)
        print(result)

    if Cal[1] == "*":
        a = int(Cal[0])
        b = int(Cal[2])
        result = mul(a,b)
        print(result)

    if Cal[1] == "/":
        a = int(Cal[0])
        b = int(Cal[2])
        result = div(a,b)
        print(result)

    if Cal[0] == "":
        sys.exit()

    if Cal[1] != "+" or "-" or "*" or "/":
        print("please reenter")
        
        
        //힘들어
        






