def safe_sum(*costs):
    try:
        # We TRY to do the math
        total = sum(costs)
        return f"Total: Rs.{total}"
    except TypeError:
        # If a string was in the bag, the 'Worker' jumps here instead of crashing
        return "⚠️ Error: One of the prices is not a number! Please check your input."

# TEST IT
print(safe_sum(100, 200, 300))      # Works fine
print(safe_sum(100, "Fifty", 300))  # Catches the error!