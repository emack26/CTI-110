#Elaine Mack
#10-17-2026
#P4HW1
#Using Loop

# 1. Ask the user for the number of scores
num_scores = int(input("How many scores would you like to enter? "))

# Informatively named list to store the valid collected scores
collected_student_scores = []

# Loop to collect the exact number of scores requested
for i in range(num_scores):
    # Inner loop for input validation
    while True:
        score = float(input(f"Enter score #{i + 1} (0-100): "))
        
        # Check if the score is valid
        if 0 <= score <= 100:
            # Add valid score to the informatively named list
            collected_student_scores.append(score)
            break 
        else:
            print("Error: Invalid score. Please enter a value between 0 and 100.")

print(f"\nOriginal Scores: {collected_student_scores}")

# 2. Display the lowest score entered
lowest_score = min(collected_student_scores)
print(f"Lowest score entered: {lowest_score}")

# 3. Create and display the Score List after dropping the lowest score
# (Using a copy so the original list remains untouched if needed)
modified_scores_list = collected_student_scores.copy()
modified_scores_list.remove(lowest_score)
print(f"Score List after dropping lowest score: {modified_scores_list}")

# 4. Calculate and display the average of the scores in the modified list
if len(modified_scores_list) > 0:
    modified_average = sum(modified_scores_list) / len(modified_scores_list)
else:
    modified_average = 0.0  # Fallback if only 1 score was entered total
print(f"The average of scores in modified list: {modified_average:.2f}")

# 5. Determine the letter grade for the calculated average and display it
if modified_average >= 90:
    letter_grade = 'A'
elif modified_average >= 80:
    letter_grade = 'B'
elif modified_average >= 70:
    letter_grade = 'C'
elif modified_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Final Letter Grade: {letter_grade}")