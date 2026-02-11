def calculate_chai_bill():
    chai_price = 20 # This is LOCAL
    return f"Chai is {chai_price}"

calculate_chai_bill()

# HR QUESTION: "Can I print chai_price here?"

# print(chai_price)

#  #it will show the name error 

# corrected code 
def calculate_chai_bill():
    price = 20
    return price # Sending the value across the bridge

# We catch it in a GLOBAL variable
final_price = calculate_chai_bill() 
print(f"I can see it now: {final_price}")