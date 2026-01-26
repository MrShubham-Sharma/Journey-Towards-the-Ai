# 1. THE DEFINITION: Building the "Safety Tool"
def get_valid_gift(person_name):
    """This function handles all the while-true and try-except logic once."""
    while True:
        try:
            # We use 'person_name' to customize the input prompt
            cost = int(input(f"Enter gift cost for {person_name}: "))
            
            # Applying your 'At least Rs.100' business rule
            if cost < 100:
                print("Utsav gifts must be at least Rs.100!")
                continue
                
            return cost  # This 'returns' the value and EXITS the function
        except ValueError:
            print("Error: Please enter a valid number.")

# 2. THE MAIN PROGRAM: Using the tool
total_budget = 0

print(" Utsav Gift Distribution (Day 16) ")

# Now our loops are much cleaner!
for group in ["Elders", "Cousins"]:
    print(f"\nProcessing {group}...")
    
    for i in range(1, 3): # Loops twice for Person 1 and Person 2
        # WE CALL THE FUNCTION HERE
        # The result of the function is 'saved' into the variable 'gift'
        gift = get_valid_gift(f"{group} Person {i}")
        total_budget += gift

print(f"\n FINAL TOTAL: Rs.{total_budget}")