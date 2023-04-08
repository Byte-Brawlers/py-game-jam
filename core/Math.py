from math import sqrt

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def to_tuple(self):
        return (self.x, self.y)

    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

class Transform:
    def __init__(self):
        self.position = Vector2()
        self.scale = Vector2(1, 1)


