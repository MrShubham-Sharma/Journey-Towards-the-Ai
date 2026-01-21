# for reset grand total 
grand_total = 0

# outer loop 
for days in ["Monday", "Tuesday"]:
    daily_total = 0  #This is the "Reset"
    print(f"Processing: {days} ")
    
    # inner lopp
    for materials in ["Cement", "Steel"]:
        cost = int(input(f"Enter cost for {materials} on {days}: "))
        daily_total += cost
        grand_total += cost

        # final verification
    print(f"Total spent on {days}: {daily_total}")

# grand total
print(f"\n GRAND TOTAL for the site: {grand_total}")