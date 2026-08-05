class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def from_tuple(cls, t):
        return cls(t[0], t[1])

    @staticmethod
    def distance(p1, p2):
        return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2) ** 0.5

p = Point.from_tuple((3, 4))
