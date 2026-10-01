#ElaineMack
#10/01/2026
#P3HW2
#salary calculator

#request employee information
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#calculate overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
    total_pay = regular_pay + overtime_pay

print(f"Employee Name: {employee_name}")
print(f"Hours Worked: {hours_worked}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Total Pay: ${total_pay:.2f}")