# Total Saving Resetor
trip_pot = 0

# outer loop for day
for Day in ["Day 1","Day 2", "Day 3"]:

    # daily_savings reseter
    daily_savings =0
    print(f" the saving of the {Day}")

    #Inner Loop For Firends
    for Friends in ["Rohit","Parth","Shubham"]:

        # The ammount Input 
        Ammount = int(input(f"How much {Friends} Saved in Today ?:"))

        # if condition for Savings where > 200
        if Ammount > 200:
            print("That's The Big Saving Today")
        
        # mathamatical Calculator
        daily_savings += Ammount
        trip_pot += Ammount
    
    # print the day and daily saving
    print(f"\n The saving of the {Day} : {daily_savings}")

# The final Savings
print(f"\n The Total Savings of all Day's is {trip_pot}.Rs ")