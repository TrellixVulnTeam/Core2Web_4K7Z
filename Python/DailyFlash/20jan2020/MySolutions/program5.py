
'''
Write a Program to print following Pattern.
Output:
0 0 0 0
1 1 1 1
0 0 0 0
1 1 1 1

'''

for i in range(4):
	for j in range(4):
		if(i%2==0):
			print('0',end=" ")
		else:
			print('1',end=" ")
	print()


