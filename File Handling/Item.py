new_items = ["Steel", "Water", "Plumbing"]

# We use 'with' so we don't have to worry about .close()
with open("Material.txt", "a") as site_file:
    for item in new_items:
        # We write the item + a new line so they don't stick together
        site_file.write(item + "\n") 

print("All items from the list are now in your file!")