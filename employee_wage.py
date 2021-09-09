import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4


def emp_check(argument):
    switcher = {
        0:
            "Employee worked full time and the wage is " + str(WAGE_PER_HOUR * FULL_TIME),
        1:
            "Employee worked part time and the wage is " + str(WAGE_PER_HOUR * PART_TIME),
        2:
            "Employee is absent"
    }
    return switcher.get(argument, "nothing")


attendance = random.randint(0, 2)
print(emp_check(attendance))