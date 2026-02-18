# Note the \n inside the list items
pro_items = ["Electrical\n", "Painting\n", "Tiling\n"]

with open("Site Audit.txt", "a") as site_file:
    site_file.writelines(pro_items)