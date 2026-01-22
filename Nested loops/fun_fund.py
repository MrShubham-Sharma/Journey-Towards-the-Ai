trip_pot = 0
for Day in ["Day 1","Day 2", "Day 3"]:
    daily_savings =0
    print(f" the saving of the {Day}")
    for Friends in ["Rohit","Parth","Shubham"]:
        Ammount = int(input(f"How much {Friends} Saved in Today ?:"))
        if Ammount > 200:
            print("That's The Big Saving Today")
        daily_savings += Ammount
        trip_pot += Ammount
    print(f"\n The saving of the {Day} : {daily_savings}")
print(f"\n The Total Savings of all Day's is {trip_pot}.Rs ")