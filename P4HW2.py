#ElaineMack
#10/17/2026
#P4HW2
#salary calculator with loops

# Initialize variables to keep track of cumulative totals across all employees
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
total_employees = 0

# Define constants for standard payroll rules
STANDARD_HOURS_LIMIT = 40.0
OVERTIME_RATE_MULTIPLIER = 1.5

print("--- Employee Payroll Processing System ---")
print("Enter 'Done' as the employee name when you are finished.\n")

# ==========================================
# SENTINEL LOOP (INPUT & PROCESSING)
# ==========================================
while True:
    # Prompt the user to enter the employee's name
    employee_name = input("Enter employee name (or 'Done' to finish): ").strip()
    
    # Check the sentinel condition to terminate the loop
    # The program stops ONLY when the name entered is exactly "Done"
    if employee_name == "Done":
        break
        
    # Input validation: Ensure the name is not empty
    if not employee_name:
        print("Employee name cannot be empty. Please try again.\n")
        continue

    # Get payroll inputs from the user with basic error handling
    try:
        pay_rate = float(input(f"Enter hourly pay rate for {employee_name}: $"))
        hours_worked = float(input(f"Enter total hours worked for {employee_name}: "))
        
        if pay_rate < 0 or hours_worked < 0:
            print("Pay rate and hours worked must be positive numbers. Please restart this employee entry.\n")
            continue
    except ValueError:
        print("Invalid input. Please enter numbers for pay rate and hours. Restarting entry...\n")
        continue

    # ==========================================
    # CALCULATIONS FOR INDIVIDUAL EMPLOYEE
    # ==========================================
    # Initialize individual pay variables
    regular_hours = 0.0
    overtime_hours = 0.0
    
    # Determine regular and overtime hours
    if hours_worked > STANDARD_HOURS_LIMIT:
        regular_hours = STANDARD_HOURS_LIMIT
        overtime_hours = hours_worked - STANDARD_HOURS_LIMIT
    else:
        regular_hours = hours_worked
        overtime_hours = 0.0

    # Compute individual pay amounts
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * OVERTIME_RATE_MULTIPLIER)
    gross_pay = regular_pay + overtime_pay

    # Display individual breakdown for clarity
    print(f"  -> Regular Pay: ${regular_pay:,.2f}")
    print(f"  -> Overtime Pay: ${overtime_pay:,.2f}")
    print(f"  -> Gross Pay: ${gross_pay:,.2f}\n")

    # ==========================================
    # ACCUMULATING RUNNING TOTALS
    # ==========================================
    # Add current employee's figures to the master tracking variables
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    total_employees += 1


# ==========================================
# FINAL OUTPUT DISPLAY
# ==========================================
# This section executes only after the user breaks out of the loop by typing "Done"
print("\n==========================================")
print("FINAL SUMMARY REPORT")
print("==========================================")
print(f"Total Employees Processed : {total_employees}")
print(f"Total Regular Pay         : ${total_regular_pay:,.2f}")
print(f"Total Overtime Pay        : ${total_overtime_pay:,.2f}")
print(f"Total Gross Pay           : ${total_gross_pay:,.2f}")
print("==========================================")


