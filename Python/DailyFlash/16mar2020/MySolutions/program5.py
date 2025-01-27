'''
Write a Program that computes radius of a In-circle inside a triangle
if user enters the vertices of all three points of that triangle.
{Steps:
1. Calculate Radius R of an In-Circle enclosed under Triangle using
Heron’s formula :
R = (A / P)
Where,
- A is Area of that triangle
- P is semi-perimeter of Triangle
}
Input:
A (x1, y1) = 5 2
B (x2, y2) = 6 3
C (x3, y3) = 3 1
Output:
Length AB = 1.41
Length BC = 3.60
Length AC = 2.23
Perimeter of Triangle = 7.24
Semi-Perimeter of Triangle = 3.62
Area of Triangle = 0.4716
Radius of In-circle = 0.1302

'''
x1,y1=[ float(x) for x in input("A(x1,y1):").split()]
x2,y2=[float (x) for x in input("B(x2,y2):").split()]
x3,y3=[float (x) for x in input("C(x3,y3):").split()]
d1=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**(0.5)
d2=((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))**(0.5)
d3=((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))**(0.5)
print("Length of AB=",d1)
print("Length of BC=",d2)
print("Length of AC=",d3)

p=d1+d2+d3
print(" Perimeter of Triangle:",p)

s=p/2
print("Semi-perimeter of triangle=",s)

a=(s*(s-d1)*(s-d2)*(s-d3))**(0.5)
print("Area of triangle=",a)

r=(a/s)
print("Radius of In-circle=",r)
