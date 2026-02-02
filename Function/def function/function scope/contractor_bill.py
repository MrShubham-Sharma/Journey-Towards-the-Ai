# Triple Input machine. Your father needs a bill for Cement, Sand, and Transport.
# def define machine and input are cement sand and transport 
def Bill_of_Material(cement, sand, transport):
    total_ammount = cement + sand + transport
    return total_ammount
total_bill = Bill_of_Material(800,700,300)
print(f"the total Bill of the Day is Rs.{total_bill}")

def smart_bill(material_cost,Tax_persentage):
    Tax_ammount = material_cost * Tax_persentage / 100
    total_cost = material_cost + Tax_ammount
    return total_cost
bill_with_tax = smart_bill(400,18)
print(f"The Total Cost MRP.Rs.{bill_with_tax:.2f}")