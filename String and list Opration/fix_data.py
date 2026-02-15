# FIXED data (Immutable Tuple)
locations = ("Darjeeling", "Gangtok", "Siliguri")

# LIVE data (Mutable List)
friends = ["Rohit", "Parth"]

def update_trip_data(new_friend, index_to_change):
    try:
        # Update the list (Allowed)
        friends.append(new_friend)
        
        # Try to change the Tuple (Not Allowed - will trigger Except)
        locations[index_to_change] = "Sikkim" 
        
    except TypeError:
        print("🛡️ Safety Triggered: You cannot change a Tuple location!")
        
    return f"Current Friends: {friends} | Planned Locations: {locations}"

# Test the logic
print(update_trip_data("Shubham", 0))