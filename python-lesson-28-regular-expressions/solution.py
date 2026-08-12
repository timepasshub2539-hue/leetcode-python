import re

pattern = r"(?P<area>\d{3})[-.\s]?(?P<exch>\d{3})[-.\s]?(?P<line>\d{4})"

user_input = "(555) 123-4567"

if m := re.search(pattern, user_input):
    print("valid, area code:", m.group('area'))
else:
    print("not a phone number")
