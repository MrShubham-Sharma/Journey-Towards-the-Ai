# Raw messy data from a site audit
raw_materials = "Cement, Sand, Bricks, Cement, Sand "

# 1. Clean and split into a list
material_list = [m.strip().title() for m in raw_materials.split(",")]

# 2. Use a SET to remove duplicates (The 'Unique' Bag)
unique_materials = set(material_list)
print(f"Unique Materials identified: {unique_materials}")

# 3. Engineering Math: Floor Division
budget = 10000
price_per_bag = 1500
total_bags = budget // price_per_bag # Calculates full bags only

print(f"With Rs.{budget}, you can buy {total_bags} full bags of cement.")