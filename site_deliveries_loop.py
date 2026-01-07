site_deliveries = [2500, 12000, 1800, 10000]
rejected_trucks = 0
for bricks in site_deliveries:
    if bricks <= 3000:
        rejected_trucks = rejected_trucks +1
        print("REJECTED: Truck had only " + str(bricks) + " bricks")
print("Total Trucks Rejected today: " + str(rejected_trucks))