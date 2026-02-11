def check_immutable(*costs):
    print(f"The data type of your bag is: {type(costs)}")
    try:
        # Tuples are IMMUTABLE - you cannot change them!
        costs[0] = 5000 
    except TypeError:
        return "❌ Verified: You cannot change prices inside a Tuple bag!"

print(check_immutable(1000, 2000, 3000))