class Cart:
    def __init__(self):
        self.total = 0
    def add(self, price):
        self.total += price * 1.08
