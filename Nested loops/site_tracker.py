grand_total = 0  # Level 1: Lives forever

for day in ["Day 1", "Day 2"]:
    daily_total = 0  # Level 2: Resets every day
    
    for material in ["Bricks", "Sand"]:
        cost = int(input(f"Enter cost {day} for {material}: "))
        # Level 3: Add to both!
        daily_total += cost
        grand_total += cost
        
    # This print should happen AFTER the materials are done, 
    # but BEFORE the next day starts. (Line up with the 'for material')
    print(f"Total spent on {day}: {daily_total}")

# This print should happen ONLY ONCE at the very end.
# (Line up with the first 'for day')
print(f"Final Project Total: {grand_total}")