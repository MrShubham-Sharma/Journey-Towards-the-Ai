# 1. THE MANUAL (The Instruction)
def calculate_chai_bill(chai_price, *snacks):
    # 'chai_price' is a normal locker.
    # '*snacks' is the Burlap Sack (Tuple).
    
    print(f"--- Processing Bill ---")
    
    # The worker reaches into the sack and adds up the snack prices
    total_snacks = sum(snacks) 
    
    final_amount = chai_price + total_snacks
    
    # The worker hands the final result back to you
    return final_amount

# 2. THE WORKER IN ACTION (Running the code)
# We 'catch' the result in a locker called 'my_payment'
my_payment = calculate_chai_bill(20, 15, 10, 30)

# 3. THE DISPLAY
print(f"Total to pay the Chai-wala: Rs.{my_payment}")