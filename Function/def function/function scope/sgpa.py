college_name = "SLRTCE"

def check_eligibility(my_sgpa):
    if my_sgpa >= 6.0:
        return "Eligible"
    else:
        return "Not Eligible"

# Use your real Sem 5 SGPA (6.74) here!
status = check_eligibility(6.74)
print(f"At {college_name}, your status is: {status}")