# Elaine Mack
#09/10/2026
# p1hw2_MackElaine.py
# basic math operations

total_budget = float(input("Enter your total budget: "))
destination = input("Enter your travel destination: ")
gas_cost = float(input("Enter the cost of gas: "))
acconmodation_cost = float(input("Enter the cost of accommodation: "))
food_cost = float(input("Enter the cost of food: "))

total_expenses = gas_cost + acconmodation_cost + food_cost
remaining_budget = total_budget - total_expenses

print("\n------Travel Budget Summary----")
print("destination:", destination)
print("Total Budget: $", total_budget)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)