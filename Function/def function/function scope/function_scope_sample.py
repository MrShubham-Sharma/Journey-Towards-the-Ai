# GLOBAL VARIABLE (Everyone can see this)
trip_name = "Darjeeling 2026"

def calculate_budget(train_fare, stay_fare):
    # LOCAL VARIABLE (Only exists inside this function)
    total = train_fare + stay_fare
    return total

# Using the function
print(f"Planning for: {trip_name}")
print(f"Total: {calculate_budget(1500, 3000)}")

# ERROR CHECK: If I try to print 'total' here, it will crash.
# print(total) # Python says: "I don't know what 'total' is!"