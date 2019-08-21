#Python program to find the area of a triangle

a = 5
b = 6
c = 7

#Get lengths from user:

#To ask month and year from the user:
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

#Calculate the semi-perimeter
s = (a + b + c) / 2

#Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Print the answer
print("\n\nThe area of the triangle is: %0.2f" %area)
