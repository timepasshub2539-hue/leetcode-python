students = [{'name':'Sam','score':72}, {'name':'Ana','score':91}]
for i in range(len(students)):
    for j in range(len(students)-1):
        if students[j]['score'] < students[j+1]['score']:
            students[j], students[j+1] = students[j+1], students[j]
