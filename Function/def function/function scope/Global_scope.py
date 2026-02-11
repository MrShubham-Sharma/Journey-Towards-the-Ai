# GLOBAL variable (Visible to everyone)
total_budget = 10000 

def add_expense(amount):
    # LOCAL variable (Only exists inside this function)
    remaining = total_budget - amount 
    return f"After spending Rs.{amount}, the local remaining balance is: Rs.{remaining}"

print(add_expense(2000))
# print(remaining)  <-- If you uncomment this, it will crash! (Local Scope)