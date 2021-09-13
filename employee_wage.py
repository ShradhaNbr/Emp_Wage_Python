import random

from exception import ValueTooLargeError, ValueTooSmallError

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4


class Employee:
    @staticmethod
    def calculate_wage():
        emp_attendance = {
            0:
                0,
            1:
                FULL_TIME,
            2:
                PART_TIME
        }
        days_worked = 0
        hours_worked = 0
        try:
            total_working_days = int(input("Enter total number of working days\n"))
            total_working_hours = int(input("Enter total number of working hours\n"))
            if total_working_days > 30 or total_working_hours > 250:
                raise ValueTooLargeError
            elif total_working_days < 5 or total_working_hours < 50:
                raise ValueTooSmallError
            while days_worked < total_working_days and hours_worked < total_working_hours:
                attendance = random.randint(0, 2)
                hours_worked = hours_worked + emp_attendance.get(attendance)
                days_worked = days_worked + 1
        except ValueError:
            print("Please enter a valid input !!!")
        except ValueTooLargeError:
            print("Value is too large. Please enter a smaller value")
        except ValueTooSmallError:
            print("Value is too small. Please enter a larger value")
        return WAGE_PER_HOUR * hours_worked


if __name__ == "__main__":
    emp = Employee()
    total_wage = emp.calculate_wage()
    print("Total employee wage ", total_wage)
