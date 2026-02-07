# machine input 
def site_audit(**expenses):
    # bill header
    print(f"---- Bill Receipt -----")

    # name is just like comment and price expence count price
    for name, price in expenses.items():
        print(f"{name}: Rs.{price}")
    
    # the total count of bill
    total = sum(expenses.values())
    print(f"-------------------")
    
    # return will hold the number 
    return total

report = site_audit(Cement=2000, Sand=1500, Labor=5000)
print(f"Stored total for database: Rs.{report}")