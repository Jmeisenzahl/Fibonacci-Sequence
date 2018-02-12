A=0
B=1
C=1
counter = 1

while(counter<=25):
	print(str(counter) + " : " + str(C))
	C = A + B
	A = B
	B = C
	counter = counter + 1