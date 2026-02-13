from math import sqrt  # Specific import to save memory on your Lenovo LOQ

def calculate_site_dimension(*measurements):
    try:
        # We sum the 'Vacuum Bag' first
        total_area = sum(measurements)
        
        # Calculate the side length of a square area
        side_length = sqrt(total_area)
        return f"For a total area of {total_area} sq.ft, the side length is: {side_length:.2f} ft."
    
    except TypeError:
        return "❌ Error: Please ensure all measurements are numbers, not text!"

# Commit this test
print(calculate_site_dimension(400, 600, 1000))
print(calculate_site_dimension(400, "Error", 1000))