from array import *
list1=[int(x)for x in input("Enter elements:").split()]
arr=array('i',list1)
s=1
for i in range(len(arr)):
	if(arr[i]%2==0):
		s=s*arr[i]
print(s,end=" ")
