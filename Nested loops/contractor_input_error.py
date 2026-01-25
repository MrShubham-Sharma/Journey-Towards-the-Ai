# the value Resetor for tatal value 
grand_total =0

# inner loop for the Rooms
for Room in ["Kitchen","Hall","Bedroom"]:

    # vlaue restor for the Room Total
    room_total = 0
    print(f"the budget of the {Room}")

    # Inner loop for the Material
    for Material in ["Cement","Sand","Bricks"]:
        
        # the condition for the input 
        try:
            cost = int(input(f"Enter the cost of the {Material} for {Room} :"))
            grand_total += cost
            room_total += cost

        #if the input is wrong or get skipped then it will show tis error meassege  
        except:
              print(f"Unexpected eroor you try variable / you skip the input")
    
    print(f"The cost of the {Room} is Rs.{room_total} ")
print(f"The Final Budget Of Project is Rs.{grand_total} ")