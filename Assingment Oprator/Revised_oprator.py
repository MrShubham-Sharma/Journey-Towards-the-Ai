total_units = 157
package_size = 10

# Standard Division (Float)
ratio = total_units / package_size

# Floor Division (Whole packages)
full_packages = total_units // package_size

# Modulus (Remaining units)
leftover_units = total_units % package_size

print(f"Standard: {ratio} | Floor: {full_packages} | Modulus: {leftover_units}")