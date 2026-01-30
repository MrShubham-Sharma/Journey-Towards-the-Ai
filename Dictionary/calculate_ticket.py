# 'def' creates the machine. 
# It needs two 'ingredients': price and is_student (True or False)
def calculate_ticket(price, is_student):
    if is_student == True:
        discount = price * 0.40  # 40% Discount
        final_price = price - discount
        return final_price       # Handing the discounted price back
    else:
        return price             # Handing the full price back

# USING THE MACHINE

# Scenario 1: You (A Student) traveling on Tapovan
my_ticket = calculate_ticket(500, True) 
print(f"Shubham's Student Ticket: Rs.{my_ticket:.2f}")

# Scenario 2: A regular passenger
normal_ticket = calculate_ticket(500, False)
print(f"Regular Ticket: Rs.{normal_ticket:.2f}")