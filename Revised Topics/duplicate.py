# Topic: String Methods, Sets, and Floor Division
raw_materials = "  sand, cement, bricks, sand  "

# 1. Clean and remove duplicates (Set)
unique_materials = {item.strip().title() for item in raw_materials.split(",")}
print(f"Audit List: {unique_materials}")

# 2. Engineering Math (Floor Division & Modulus)
total_budget = 5000
cost_per_item = 1200

can_buy = total_budget // cost_per_item
remaining_cash = total_budget % cost_per_item

print(f"Affordable Units: {can_buy} | Leftover: ₹{remaining_cash}")