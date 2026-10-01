#Elaine Mack
#10/01/2026
#P3HW1
#Debugging



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
grades = [float(grade) for grade in grades]
lowest = min(grades)
highest = max(grades)
sum = sum (grades)
avg = sum / len(grades)

# determine letter grade for average
if avg >= 90:
    letter_grade = 'A'

elif avg >= 80:
    letter_grade = 'B'
else:
    letter_grade = 'F'


print(f"Your grade is: {letter_grade}")
