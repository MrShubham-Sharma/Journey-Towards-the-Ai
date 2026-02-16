# Raw input with spaces and duplicates
raw_data = "  cement, sand, bricks, cement, SAND "

# 1. Clean and separate (String Methods)
cleaned_list = [item.strip().title() for item in raw_data.split(",")]

# 2. Remove duplicates (Set Operation)
unique_audit = set(cleaned_list)

print(f"Original: {raw_data}")
print(f"Cleaned & Unique: {unique_audit}")