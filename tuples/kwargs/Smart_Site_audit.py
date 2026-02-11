def check_material(material_name, **stock):
    # .get() is a pro way to check for a key without crashing
    price = stock.get(material_name, "Not Found")
    
    if price != "Not Found":
        return f"Current price for {material_name} is Rs.{price}"
    else:
        return f"⚠️ Warning: {material_name} is missing from the audit log."

# Test it
print(check_material("Cement", Cement=2000, Sand=1500))
print(check_material("Bricks", Cement=2000, Sand=1500))