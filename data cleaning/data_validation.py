# lengths in meters
steel_rods = [12.1, 11.9, 12.0, 10.5, 12.2] 

for length in steel_rods:
    if length < 11.0:
        print(f" REJECT BATCH: Found a rod of {length}m. Quality too low!")
        break # Exit the loop entirely
    elif length < 12.0:
        print(f" WARNING: Rod of {length}m is slightly short. Mark for secondary use.")
        continue # Skip to the next rod
    else:
        print(f" Rod {length}m: Perfect quality.")


savings = 0
target = 50000
month = 1

while savings < target:
    # Simulating adding money each month
    amount = int(input(f"Month {month}: How much did you save? "))
    savings = savings + amount # The Running Total
    
    print(f"Total Savings: {savings}")
    
    if savings >= target:
        print("🎉 PACK YOUR BAGS! You reached the goal for Darjeeling!")
    else:
        print(f"Keep going! You need {target - savings} more.")
        month = month + 1 # Increment the month counter