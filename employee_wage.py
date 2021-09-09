import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
TOTAL_WORKING_DAYS = 20


def calculate_wage():
    emp_attendance = {
        0:
            FULL_TIME,
        1:
            PART_TIME,
        2:
            0
    }
    days_worked = 0
    while days_worked < TOTAL_WORKING_DAYS:
        attendance = random.randint(0, 2)
        days_worked = days_worked + emp_attendance.get(attendance)
    return WAGE_PER_HOUR * days_worked


total_wage = calculate_wage()
print("Total employee wage ", total_wage)