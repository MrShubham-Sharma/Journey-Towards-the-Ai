def check_expense(trip_name, **expenses):
    print(f"--- {trip_name} Audit ---")
    
    # We check if 'Food' is one of the keys in the logbook
    if "Food" in expenses:
        price = expenses["Food"]
        return f"You spent Rs.{price} on Food."
    else:
        return "No Food expense found in the logbook!"

# TEST IT
print(check_expense("Darjeeling", Hotel=3000, Train=1500, Food=2000))