import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def find_distance(self,x1,y1):
        return math.sqrt(math.pow(x1-self.x,2)+ math.pow(y1-self.y,2))
    def get(self):
        return (self.x,self.y)
    def print(self):
        print(f'point is ({self.x},{self.y})')
    def visual_representation(self):
        for i in range(math.floor(math.fabs(self.y))):
            print("|")
        s = ""
        for j in range(math.floor(math.fabs(self.x))):
            s += "="
        print(s)


# x1 = float(input("Enter point x coordinate x1 ="))
# y1 = float(input("Enter point y coordinate y1 ="))
# p1 = Point(x1,y1)
# p1.print()
# x2 = float(input("Enter point x coordinate x2 ="))
# y2 = float(input("Enter point y coordinate y2 ="))
# p2 = Point(x2,y2)
# print(p1.find_distance(x2,y2))
# print(p1.find_distance(p2.x,p2.y))
# print(p2.find_distance(x1,y1))
# p1.visual_representation()
# p2.visual_representation()
#
