f = open("yesterday",'r')

DATA = f.read()

num_of_yesterday = DATA.count('yesterday')

num_of_Yesterday = DATA.count('Yesterday')

Sum_of_yesterday = num_of_Yesterday + num_of_yesterday

print("Number of A Word 'Yesterday' is " , Sum_of_yesterday)

