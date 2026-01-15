# --- 1. INPUT (Materials) ---
# Expenses: [Train, Food, Sightseeing, Emergency]
trip_expenses = [3500, 4200, 6500, 2000] 
total_cost = 0
high_expense_count = 0

# --- 2. PROCESS (The Work) ---
# We scan each expense to see if it's over budget
for cost in trip_expenses:
    total_cost = total_cost + cost
    
    # Check if a single item is more than 5000
    if cost > 5000:
        high_expense_count = high_expense_count + 1
        print("WARNING: High expense found: " + str(cost))

# --- 3. OUTPUT (The Result) ---
print("------------------------------")
print("Total Estimated Trip Cost: " + str(total_cost))
print("Total Items over ₹5000: " + str(high_expense_count))