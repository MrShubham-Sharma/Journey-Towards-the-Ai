def construction_audit(site_name, **materials):
    print(f"--- LOGBOOK FOR: {site_name} ---")
    for item, price in materials.items():
        print(f"Property: {item} | Cost: Rs.{price}")
    
    total = sum(materials.values())
    return total

# Commit this test
final_bill = construction_audit("Niphad Project", Cement=2000, Sand=1500, Bricks=5000)
print(f"Grand Total to be paid: Rs.{final_bill}")