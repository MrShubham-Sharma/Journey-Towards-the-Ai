def check_expense(trip_name, **expenses):
    print(f"--- {trip_name} Audit ---")
    
    # We check if 'Food' is one of the keys in the logbook
    for name, cost in expenses.items():
        print(f"{name} Rs.{cost}")
    total =sum(expenses.values())
    print("---------------")
    return total

# TEST IT
Total_cost =check_expense("Darjeeling", Hotel=3000, Train=1500, Food=2000)
print(f"The total Bill for all Expenses is :{Total_cost}")