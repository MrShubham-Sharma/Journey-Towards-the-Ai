# container from user 
Delivery = [1292,39403,4030,449]
# requirement for user 
requirement = 3000
# batch' starts as 1292, then becomes 39403, then 4030...
for batch in Delivery:
    # We compare the NICKNAME (the current box) to the requirement
    if batch >= requirement:
        print("Status:" +str(batch)+ " your in stock you good to go") 
    else:
        print("Status:" +str(batch)+ " your out of sock Stop!")