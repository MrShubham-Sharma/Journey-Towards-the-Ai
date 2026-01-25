grand_total = 0

for Room in ["Kitchen", "Hall"]:
    room_total = 0
    print(f"\n  Audit for {Room} ")

    for Material in ["Cement", "Sand"]:
        # START OF PERSISTENCE LOOP
        while True:
            try:
                cost = int(input(f"Enter cost for {Material} in {Room}: "))
                # If we get here, the number is valid!
                room_total += cost
                grand_total += cost
                break  # Exit the 'while' loop and move to next material
            except ValueError:
                print(f" ERROR: Please enter a numeric value for {Material}.")
        # END OF PERSISTENCE LOOP
    
    print(f" Room Total: Rs.{room_total}")

print(f"\n FINAL PROJECT TOTAL: Rs.{grand_total}")