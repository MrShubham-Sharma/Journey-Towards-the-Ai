total_cost = 0
for Pepole in ["Elders", "Cousins", "Kids"]:

    # Reset for each group
    Pepole_gifts =0
    print(f"the Group of {Pepole} ")
    for pepole_of_group in ["Person 1","Person2"]:

        # Persistence loop for 100% accuracy
        while True:
            try:
                cost = int(input(f"Enter  the {pepole_of_group} Paying the cost for gift :"))
                # Rule: At least Rs.100
                if cost <= 100:
                   print(f"Utsav gifts must be at least Rs.100! Try again")
                   continue

                # Logic: Update totals only on success
                total_cost += cost
                Pepole_gifts += cost
                break

            # Catch letters/typos
            except ValueError:
             print(f"Error :you have been enter the Wrong cost")
    print(f"The Cost of the gift for {Pepole} : {Pepole_gifts}")
print(f"The Final Distribution Of is Rs.{total_cost}")