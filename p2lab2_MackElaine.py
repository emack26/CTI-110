# Elaine Mack
#09/18/2026
#P2lab2
#creating a dictionary where key and values pairs

# Create the dictionary with vehicle keys and MPG values
vehicle_data = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# 1. Print the variable that holds the keys
vehicle_keys = vehicle_data.keys()
print("Available vehicles:", list(vehicle_keys))

# 2. Prompt the user to enter one of the vehicles (case-sensitive)
selected_vehicle = input("Enter a vehicle name exactly as shown above: ")

# 3. Display the MPG for the vehicle entered
vehicle_mpg = vehicle_data[selected_vehicle]
print(f"The {selected_vehicle} gets {vehicle_mpg} MPG.")

# 4. Prompt the user to enter the number of miles to drive
miles_to_drive = float(input(f"Enter the number of miles you will drive the {selected_vehicle}: "))

# 5. Calculate the gallons of gas needed
gallons_needed = miles_to_drive / vehicle_mpg

# 6. Display the gallons of gas needed, rounded to two decimal places using an f-string
print(f"Gallons of gas needed to drive {miles_to_drive} miles: {gallons_needed:.2f}")
