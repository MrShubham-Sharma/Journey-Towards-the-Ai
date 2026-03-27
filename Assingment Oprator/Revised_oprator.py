total_units = 157
package_size = 10

# Standard Division (Float)
ratio = total_units / package_size

# Floor Division (Whole packages)
full_packages = total_units // package_size

# Modulus (Remaining units)
leftover_units = total_units % package_size

print(f"Standard: {ratio} | Floor: {full_packages} | Modulus: {leftover_units}")

# Topic: Comparison and Logical Operators
stock_count = 50
minimum_required = 40
is_urgent = False

# Comparison Operators: Checking thresholds
has_enough_stock = stock_count >= minimum_required

# Logical Operators: Combining conditions
# Work can start if we have enough stock AND it is either urgent OR we have high stock
should_start = has_enough_stock and (is_urgent or stock_count > 45)

print(f"Enough Stock? {has_enough_stock}")
print(f"Process Started? {should_start}")