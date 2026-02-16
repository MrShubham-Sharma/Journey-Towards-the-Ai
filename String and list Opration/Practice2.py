# Fixed Locations (Tuple)
locations = ("Darjeeling", "Gangtok", "Siliguri")

def update_itinerary(new_place):
    try:
        # Attempting to change an immutable Tuple
        locations[0] = new_place
    except TypeError:
        return "🛡️ Security: Locations are fixed and cannot be modified!"

print(update_itinerary("Sikkim"))
print(f"Verified Locations: {locations}")