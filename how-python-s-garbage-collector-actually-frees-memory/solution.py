import sys
user = {"name": "Kai"}
print(sys.getrefcount(user))
other = user
print(sys.getrefcount(user))
