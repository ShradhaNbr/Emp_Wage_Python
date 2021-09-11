WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
TOTAL_WORKING_DAYS = 20
TOTAL_WORKING_HOURS = 100


class Employee:
    def calculate_wage(self):
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
        while days_worked < TOTAL_WORKING_DAYS and hours_worked < TOTAL_WORKING_HOURS:
            try:
                attendance = int(input("Enter the attendance 0.Absent 1.Full- time 2. Part-time \n"))
                hours_worked = hours_worked + emp_attendance.get(attendance)
                days_worked = days_worked + 1
            except:
                print("Please enter a valid input !!!")
        return WAGE_PER_HOUR * hours_worked


if __name__ == "__main__":
    emp = Employee()
    total_wage = emp.calculate_wage()
    print("Total employee wage ", total_wage)
