for days in ["Monday", "Tuesday"]:
    daily_total = 0  #This is the "Reset" we discussed!
    print(f"--- Processing: {days} ---")
    
    for materials in ["Cement", "Steel"]:
        grand_total = 0
        cost = int(input(f"Enter cost for {materials} on {days}: "))
        daily_total += cost
        grand_total += cost
        
    print(f"Total spent on {days}: {daily_total}")

print(f"\n GRAND TOTAL for the site: {grand_total}")