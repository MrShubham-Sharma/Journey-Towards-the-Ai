base_price = 100
tax_rate = 0.05

# Assign the result of a calculation to a new variable
total_price = base_price + (base_price * tax_rate)

print(f"The total price is: {total_price}")

# Starting balance
account_balance = 500.00

# Using augmented assignment operators to update the value
deposit = 150.0
account_balance += deposit  # Equivalent to: account_balance = account_balance + deposit

withdrawal = 50.0
account_balance -= withdrawal  # Equivalent to: account_balance = account_balance - withdrawal

print(f"Updated Balance: ${account_balance}")