# GLOBAL variable (The Master Budget)
remaining_budget = 7000  # Your Darjeeling trip budget

def add_travel_expense(item_name, cost):
    global remaining_budget  # Accessing the 'College Notice Board'
    
    # LOCAL logic
    if cost > remaining_budget:
        return f"⚠️ Warning: Cannot buy {item_name}. It costs Rs.{cost}, but you only have Rs.{remaining_budget}!"
    else:
        remaining_budget -= cost
        return f"✅ Purchased {item_name} for Rs.{cost}. Remaining: Rs.{remaining_budget}"

# Commit these tests to see the budget change
print(add_travel_expense("Train Ticket", 1500))
print(add_travel_expense("Luxury Hotel", 8000))