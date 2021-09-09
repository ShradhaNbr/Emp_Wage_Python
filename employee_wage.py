import random

wage_per_hour = 20
print("Welcome to Employee Wage Computation Program")
attendance = random.randint(0, 1)
if attendance == 0:
    print("Employee is present")
    full_day = 8
else:
    print("Employee is absent")
    full_day = 0
wage = wage_per_hour * full_day
print("Employee wage ", wage)