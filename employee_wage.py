import random

print("Welcome to Employee Wage Computation Program")
attendance = random.randint(0, 1)
if attendance == 0:
    print("Employee is present")
else:
    print("Employee is absent")