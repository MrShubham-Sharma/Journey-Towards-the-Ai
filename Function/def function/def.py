# 1. Define the 'Tool' (The Function)
def get_safe_number(prompt_message):
    while True:
        try:
            value = int(input(prompt_message))
            if value < 0:
                print(" Values cannot be negative.")
                continue
            return value # This 'sends' the number back to the main code
        except ValueError:
            print(" Invalid input. Please enter a number.")

# 2. Use the 'Tool' in your Journey
print(" Modular Auditor ")

# Now, instead of 10 lines of try-except, you only need ONE line:
cement_cost = get_safe_number("Enter Cement Cost: ")
sand_cost = get_safe_number("Enter Sand Cost: ")

total = cement_cost + sand_cost
print(f"Total: {total}")