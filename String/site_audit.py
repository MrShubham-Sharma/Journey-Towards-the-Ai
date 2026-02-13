materials = ["Cement", "Sand"]

# 1. ADD to the end
materials.append("Bricks") 

# 2. INSERT at a specific spot (index 0 is the start)
materials.insert(0, "Steel") 

# 3. REMOVE by name
materials.remove("Sand")

# 4. SORT alphabetically
materials.sort()

print(materials) # Output: ['Bricks', 'Cement', 'Steel']