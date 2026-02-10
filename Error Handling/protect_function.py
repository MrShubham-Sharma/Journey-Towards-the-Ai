def travel_cost_per_head(total_bill, total_friends):
    try:
        # Ground Level: Attempting the calculation
        cost = total_bill / total_friends
        return f"Success: Each friend owes Rs.{cost}"
    
    except ZeroDivisionError:
        return " Error: You can't travel with 0 friends! Check your input."
    
    except TypeError:
        return "Error: Please use numbers only. Words don't work in math!"

# Test scenarios
print(travel_cost_per_head(5000, 4))      # Normal
print(travel_cost_per_head(5000, 0))      # Zero Error
print(travel_cost_per_head(5000, "Four")) # Type Error