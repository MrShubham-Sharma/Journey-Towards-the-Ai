from math import sqrt 
def get_audit_root(*total_cost):
    return sqrt(400)
print(get_audit_root())

from math import sqrt 

def get_audit_root(*total_costs):
    try:
        # Step 1: Sum the 'Vacuum Bag' to get ONE number
        grand_total = sum(total_costs) 
        
        # Step 2: Hand that ONE number to the specialist
        result = sqrt(grand_total)
        return result
        
    except TypeError:
        return "❌ Error: One of the costs is not a number!"

# Test it with multiple numbers
print(f"The audit root is: {get_audit_root(400, 6000, 400)}")