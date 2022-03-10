import json

file = open("students.json")
data = json.load(file)
print(data)

for student in data["students"]:
    print(student["Firstname"])

import json
videjais = 0
file = open("students.json")
data = json.load(file)
averageage = 0
cilveki = 0
for student in data["Students"]:
    averageage += int(student["Age"])
    cilveki += 1
videjais = averageage / cilveki
print(f"Cilvēku vidējais vecums ir {videjais} gadi")


count = 0
total_age = 0
for student in data["Students"]:
    total_age += int(student["Age"])
    count += 1
print(f"Average age: {total_age/count}")
