#Reset the grand total
grand_total = 0


# days of activiy
for day in ["Day1","Day2","Day3","Day4","Day5"]:
    
    # Reset the daily total
    daily_total = 0
    print(f"The epxence of {day}: ")

    # for loop for the activity
    for Activity in ["Food","Travel","Rent"]:

        # the input for budget and acivity
        cost = int(input(f"Enter the cost of {day} for the {Activity} :"))
        if cost <= 500:
            print(f"the cost of in budget{Activity}")
        else :
            print(f"The cost of the over budget is {cost} ")
            
            # daily_toatal for add in cost count
            # grand_total for add in cost count 
            daily_total +=cost
            grand_total +=cost
    
    # printing the daily total
    print(f"the Expence of the {day} : {daily_total}")

# final grand_total    
print(f"Final Audit Total: {grand_total}")