# data from user we get
site_deliveries = [2500, 12000, 1800, 10000]
# we strat count from 0
rejected_trucks = 0
# did fro loop for bricks where its in stock count
for bricks in site_deliveries:
    if bricks <= 3000:
        # if the truck has low bricks then it will be count as +1 
        rejected_trucks = rejected_trucks +1
        print("REJECTED: Truck had only " + str(bricks) + " bricks")
# it will print the single combined count 
print("Total Trucks Rejected today: " + str(rejected_trucks))