class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
