# the resetor
Room_total = 0

# Outer loop
for Room in ["Bedroom","Bathroom","kitchen","Hall"]:
    print(f"The Budget of The {Room} ! ")
    budget_cost = 0

    # Outer Loop 
    for Material in ["Cement","Tiles","Steel","Sand"]:
        Cost = int(input(f"What is the Budegt of the {Material} ? :"))

        # we use if else conditon for the responce
        if Cost > 2000:
            print(f"We Need To Talk Owner for The {Material} Budget Rs.{Cost} ")
        else:
            print(f"The {Material} Budget is in The Limit ")

            # this will Act as Notbook Where It will Add Each Entry
        Room_total += Cost
        budget_cost += Cost
        print(f"The Budegt Of The {Room} is: Rs.{budget_cost}")

# this will give use total budget
print(f"We Got The Total Budget of All around Rs.{Room_total}")