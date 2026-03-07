materials = ["Cement", "Sand", "Bricks", "Cement", "Steel", "Sand"]
materials.append("Water")
New_list = set(materials)
if "Cement" in New_list:
    print(f"Cement was Found")
print(New_list)