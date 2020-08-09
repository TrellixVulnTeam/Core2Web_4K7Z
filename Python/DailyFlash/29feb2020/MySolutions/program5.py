'''
Write a Program calculates length of all three sides of a triangle if
user provides the three points that triangle bound in.
{Note: Use Distance formula for computing the distances.}
Input:
A (x1, y1) = 5 2
B (x2, y2) = 6 3
C (x3, y3) = 3 1
Output:
Length AB = 1.41
Length BC = 3.60
Length AC = 2.23

'''

x1,y1=[int (x) for x in input("A(x1,y1)=").split()]
x2,y2=[int (y) for y in input("B(x2,y2)=").split()]
x3,y3=[int (z) for z in input("C(x3,y3)=").split()]

AB=(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))**(0.5)
print("Length AB=",AB)

BC=(((x3-x2)*(x3-x2))+((y3-y2)*(y3-y2)))**(0.5)
print("Length AB=",BC)

AC=(((x3-x1)*(x3-x1))+((y3-y1)*(y3-y1)))**(0.5)
print("Length AB=",AC)
