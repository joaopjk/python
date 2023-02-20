import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y)**2) ** 0.5


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


point = Point(3, 4)
point_2 = Point(3, 3)
# result = point.falls_in_rectangle((5, 6), (7, 9))
# print(result)
result = point.distance_from_point(point_2)
print(result)
rectangle = Rectangle(Point(5, 6), Point(7, 9))
result = point.falls_in_rectangle(rectangle)
print(result)
