import random

wage_per_hour = 20
attendance = random.randint(0, 2)
if attendance == 0:
    print("Employee worked full time")
    hours_worked = 8
elif attendance == 1:
    print("Employee worked part time")
    hours_worked = 4
else:
    print("Employee is Absent")
    hours_worked = 0
wage = wage_per_hour * hours_worked
print("Employee wage ", wage)