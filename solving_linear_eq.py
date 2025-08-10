#this program for converting one integer to another integer
#let the smallest be x and y is the largest
#we need equation y = mx +b to find both b, and m
print("x1=")
x1 =int( input())
print("x2 =")
x2 = int(input())
if x1 > x2:
	x = int(x2)
	y = int(x1)
else:
	x = int(x1)
	y = int(x2)
#we need to find y = mx +b the integer value of both b and m
b = y % x
m = int((y-b)/x)
print("the solution of y = mx + b such that x = %d, y = %d is " % (x,y))
print(" b = %d, m = %d " % (b,m))
z = input()
	