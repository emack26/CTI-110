#Elaine Mack
#10-17-2026
#P4Lab2
#Use while loop and for loop together

while True:
    try:
        num = int(input("Enter an integer: "))
        
        if num < 0:
            print("Negative values are not accepted.")
        else:
            print(f"\nMultiplication Table for {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
                
    except ValueError:
        print("Please enter a valid integer.")
        continue

    choice = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Program ended.")
        break
    