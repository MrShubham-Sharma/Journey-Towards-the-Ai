raw_data = "  cement, sand, bricks, cement  "

# 1. Clean and convert to a unique Set
cleaned_materials = {item.strip().title() for item in raw_data.split(",")}
print(f"Unique Materials: {cleaned_materials}")

# 2. Budget Logic (Floor Division & Modulus)
total_budget = 25000
item_cost = 3200

units = total_budget // item_cost
remainder = total_budget % item_cost

print(f"Units affordable: {units} | Leftover budget: ₹{remainder}")