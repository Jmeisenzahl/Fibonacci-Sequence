value = input("How many numbers in the Fibonacci Sequence do you want?: ")
a = 0
b = a + 1
for x in range(0,int(value)+1):
	print(a)
	number = a 
	a = b 
	b = number + a 	
	
