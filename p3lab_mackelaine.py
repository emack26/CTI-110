#Elaine Mack
#10/01/2026
#P3Lab
#the program will calculate the diameter, circumference, and area of a circle

#prompt  user for input
def calculate_change(amount_due, amount_paid):
    change = amount_paid - amount_due
    return change

amount = float(input("Enter the amount due: "))
print (f"Amount due: ${amount:.2f}")

#convert the amount to total cents to avoid floating point issues
total_cents = round(amount * 100)

#calculate dollars and find remaining cents
dollars = total_cents // 100
remaining_cents = total_cents % 100

#calculate quarters and find remaining cents
quarters = remaining_cents // 25
remaining_cents = remaining_cents % 25

#calculate dimes and find remaining cents
dimes = remaining_cents // 10
remaining_cents = remaining_cents % 10

#calculate nickels and find remaining cents
nickels = remaining_cents // 5
remaining_cents = remaining_cents % 5

#calculate pennies
pennies = remaining_cents

#display the results
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")
