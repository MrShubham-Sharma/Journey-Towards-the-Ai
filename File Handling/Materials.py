daily_materials = ["Wires", "Switchboard", "Bulbs"]
with open("Material.txt", "a") as site_file:
    for items in daily_materials:
        site_file.write(items+"\n")