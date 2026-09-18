#Elaine Mack
#09/18/2026
#p2hw2
#Understanding of lists

# Separate input statements for each module
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Store all six grades in a descriptive list
module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Calculate required results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_of_grades = sum_of_grades / len(module_grades)

# Display the results
print("\n--- Grade Summary ---")
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average of grades: {average_of_grades:.2f}")