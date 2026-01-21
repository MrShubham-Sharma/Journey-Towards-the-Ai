grand_total = 0

for day in ["Day1","Day2","Day3","Day4","Day5"]:
    daily_total = 0
    print(f"The epxence of {day}: ")
    for Activity in ["Food","Travel","Rent"]:
        cost = int(input(f"Enter the cost of {day} for the {Activity} :"))
        if cost <= 500:
            print(f"the cost of in budget{Activity}")
        else :
            print(f"The cost of the over budget is {cost} ")
            daily_total +=cost
            grand_total +=cost
    print(f"the Expence of the {day} : {daily_total}")
print(f"Final Audit Total: {grand_total}")