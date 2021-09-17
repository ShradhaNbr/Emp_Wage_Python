import random
import logging
import pandas as pd
from exception import ValueTooLargeError, ValueTooSmallError
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

logging.basicConfig(
    filename="employee_wage.log",
    filemode='w',
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)
log = logging.getLogger()


class Company:
    def __init__(self, wage_per_hour, company):
        self.wage_per_hour = wage_per_hour
        self.company = company

    def set_total_wage(self, total_wage):
        self.total_wage = total_wage

    def __str__(self) -> str:
        return f"Total Employee Wage for {self.company} is  {self.total_wage}"


class Employee:
    def __init__(self):
        self.company_array = []

    def add_employee(self, wage_per_hour, company):
        self.company_array.append(Company(wage_per_hour, company))

    @staticmethod
    def calculate_daily_wage(wage_per_hour, emp_hrs):
        return emp_hrs * wage_per_hour

    @staticmethod
    def check_emp_working_hours(check_emp):
        emp_attendance = {
            0: 0,
            1: FULL_DAY_HOURS,
            2: PART_TIME_HOURS
        }
        return emp_attendance.get(check_emp)

    def calculate_employee_salary(self, employee):
        working_days = 0
        total_working_hours = 0
        total_wage = 0
        try:
            number_of_working_days = int(input("Enter total number of working days\n"))
            work_hrs_per_month = int(input("Enter total number of working hours\n"))
            if number_of_working_days > 30 or work_hrs_per_month > 250:
                raise ValueTooLargeError
            elif number_of_working_days < 5 or work_hrs_per_month < 50:
                raise ValueTooSmallError
            while working_days < number_of_working_days and total_working_hours < work_hrs_per_month:
                attendance = random.randint(0, 2)
                emp_hrs = Employee().check_emp_working_hours(attendance)
                total_working_hours += emp_hrs
                working_days += 1
                total_wage += self.calculate_daily_wage(emp_hrs, employee.wage_per_hour)
            return total_wage
        except ValueError:
            logging.error("Please enter a valid input !!!")
        except ValueTooLargeError:
            log.warning("Value is too large. Please enter a smaller value")
        except ValueTooSmallError:
            log.warning("Value is too small. Please enter a larger value")

    def calculate_employee_wage(self):
        for employee in self.company_array:
            total_wage = self.calculate_employee_salary(employee)
            Company.set_total_wage(employee, total_wage)


if __name__ == "__main__":
    emp_wage = Employee()
    df = pd.read_csv("C:\\Users\\HP\\PycharmProjects\\EmployeeWage\\emp_wage.csv")
    print(df)
    # emp_wage.add_employee(20, "TCS")
    # emp_wage.add_employee(30, "Infosys")
    emp_wage.calculate_employee_wage()
    employees = "\n".join(str(employee) for employee in emp_wage.company_array)
    print(employees)
