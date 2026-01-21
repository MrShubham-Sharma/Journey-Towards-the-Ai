# grand total =0 for reset every loop
grand_total = 0

# the days for count 
for day in ["Mon", "Tue"]:

    # daily reset daily total
    daily_total = 0 

    # inner loop for materials
    for item in ["Cement", "Steel"]:
        grand_total += 10
        daily_total += 10
    # STOP HERE

print(f"total is {grand_total} and daily total is {daily_total}")
