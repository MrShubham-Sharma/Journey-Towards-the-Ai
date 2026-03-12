expenses = [1200, 1500, 800, 2200]
total_cash = 10000

# 1. Calculate the average expense (Sum / Length)
average = sum(expenses) // len(expenses)

# 2. Membership check
if 2200 in expenses:
    print("Warning: High-cost item detected in trip list.")

# 3. Floor division for capacity
room_rent = 3500
nights_allowed = total_cash // room_rent

print(f"Average Expense: ₹{average}")
print(f"With ₹{total_cash}, you can stay for {nights_allowed} nights.")