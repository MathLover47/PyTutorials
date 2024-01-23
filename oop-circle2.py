import math
from main import Point
class Circle(Point):
    pie = 3.14
    def __init__(self, radius, point):
        self.radius = radius
        self.x,self.y = point.get()
    def circumference(self):
        return 2 * self.radius * self.pie
    def area(self):
        return math.pow(self.radius,2)* self.pie
    def get(self):
        return ((self.x,self.y),radius)
    def equation(self,x):
        y = self.y + math.sqrt(-math.pow((x-self.x),2) + pow(self.radius,2))
        return y
    def get_equation(self):
        print(f"Circle Centered:({self.x},{self.y}) of radius = {self.radius}")
        print(f"(x- {self.x})^2 + (y - {self.y})^2 = {self.radius}^2")


r = float(input("Enter Radius of Circle"))
x = float(input("center x ="))
y = float(input("center y ="))
p = Point(x,y)
c = Circle(r,p)

c.print()
print("Distance between it and (10,10)")
print(c.find_distance(10,10))
c.visual_representation()
c.get_equation()
print(c.circumference())
print(c.area())
x1 = float(input("input x in domain to find image"))
y1 = c.equation(x1)
print("y="+ str(y1))
