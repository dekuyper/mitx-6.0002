import math


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Location(self.x + dx, self.y + dy)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "<{0}, {1}>".format(self.x, self.y)
