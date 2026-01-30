# FIX 1: Add '=False' to make these optional. This is a "Default Parameter."
def calculate_ticket(price, is_student=False, is_senior_citizen=False):
    if is_student:
        discount = price * 0.40
        return price - discount
    elif is_senior_citizen:
        discount = price * 0.60
        return price - discount
    else:
        return price

# --- USING THE MACHINE ---

# Scenario 1: Providing the value 'True' for student
my_ticket = calculate_ticket(500, is_student=True) 
print(f"Shubham's Student Ticket: Rs.{my_ticket:.2f}")

# Scenario 2: Providing 'False' for student, and it assumes 'False' for senior
normal_ticket = calculate_ticket(500, False)
print(f"Regular Ticket: Rs.{normal_ticket:.2f}")

# Scenario 3: Specifically telling it Senior is 'True'
old_age_ticket = calculate_ticket(500, is_senior_citizen=True)
print(f"Senior Citizen Ticket: Rs.{old_age_ticket:.2f}")