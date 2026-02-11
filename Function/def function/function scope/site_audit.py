def audit_cement(*Matetial):
    total_cement = sum(Matetial)
    return total_cement

final_bill = audit_cement(200,400,500)
print(f"The cost of Total cement is :Rs.{final_bill}")

# Sometimes, you want to change a college-wide notice from inside your room. We use the global keyword.
#  Warning: Use this sparingly; professional engineers usually hate it because it makes code messy.

budget = 5000 # Global

def spend_money(amount):
    global budget # Telling the worker to go out to the main gate
    budget = budget - amount

spend_money(1000)
print(f"New college-wide budget: {budget}")