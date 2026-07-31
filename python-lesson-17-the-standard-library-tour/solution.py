# yesterday, without stdlib
day = 17
month = 3
if day == 1:
    day = 28
    month -= 1
else:
    day -= 1

import time
seed = int(str(time.time())[-3:])
fake_random = seed % 6 + 1

user = "{'name': '" + "Kai" + "', 'age': " + str(30) + "}"
