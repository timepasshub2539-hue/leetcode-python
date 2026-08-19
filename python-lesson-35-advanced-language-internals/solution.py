class Positive:
    def __get__(self, obj, owner):
        return obj.__dict__["v"]
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("bad")
        obj.__dict__["v"] = value

class Account:
    balance = Positive()

Account().balance = 100
