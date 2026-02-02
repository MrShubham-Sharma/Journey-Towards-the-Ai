# --- THE MACHINE SHOP ---
def safety_checker(material_name):  # 1. Blueprint name & Raw material
    while True:                     # 2. The machine starts spinning
        try:
            cost = int(input(f"Enter cost for {material_name}: "))
            return cost             # 3. Product sent out! Machine stops.
        except ValueError:
            print("❌ ERROR: Use numbers only!")

# --- THE FACTORY FLOOR ---
# Now, you just press a button (Call the function)
cement = safety_checker("Cement")   # Machine runs for Cement
sand = safety_checker("Sand")       # Machine runs for Sand
bricks = safety_checker("Bricks")   # Machine runs for Bricks

print(f"Total: {cement + sand + bricks}")