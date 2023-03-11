# name = input("What's your name? ")
# logs = []
# log = input()
# log_file = open("log_file.txt", "a")
# log_file.write(f"{log}\n")
# log_file.close()
# print(log_file.closed)
# students = []
# with open("names.txt", "r") as file:
#     names = file.readlines()
    
# for name in names:
#     print(name.rstrip())
        # print(f"{name} is from {faculty}")

# for _ in range(3):
#     log = input()
#     logs.append(log)
    
# for log in logs:
#     print(f"Hi, {log}")

import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "address": row["address"]})

# def get_name(student):
#     return student["name"]

# def get_faculty(student):
#     return student["faculty"]

# for student in sorted(students, key=lambda x: x["name"], reverse=False):
#     print(f"{student['name']} is in {student['address']}")
    
name = input("What's your name? ")
address = input("What's your address? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    writer.writerow({"name": name, "address": address})