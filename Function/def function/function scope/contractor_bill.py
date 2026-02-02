# Triple Input machine. Your father needs a bill for Cement, Sand, and Transport.
# def define machine and input are cement sand and transport 
def Bill_of_Material(cement, sand, transport):
    total_ammount = cement + sand + transport
    return total_ammount
total_bill = Bill_of_Material(800,700,300)
print(f"the total Bill of the Day is Rs.{total_bill}")