# Topic: List Membership and Arithmetic Operators
inventory = ["Laptop", "Monitor", "Keyboard", "Mouse"]
search_item = "Monitor"

# 1. Membership check (Searching the list)
if search_item in inventory:
    print(f"Status: {search_item} is available in stock.")

# 2. Practical Math (Budget Allocation)
total_funds = 7500
unit_price = 1200

# How many full units can we buy?
max_units = total_funds // unit_price
# What is the remaining balance?
leftover = total_funds % unit_price

print(f"Units affordable: {max_units}")
print(f"Remaining Funds: {leftover}")