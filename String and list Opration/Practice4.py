# 1. STRING SLICING: The 'Reverse' trick
friend_name = "Rohit"
reversed_name = friend_name[::-1]
print(f"Original: {friend_name} | Reversed: {reversed_name}")

# 2. LIST METHODS: Adding and Updating
trip_friends = ["Parth", "Rohit"]
trip_friends.append("Shubham")  # Adding to end
trip_friends.sort()             # Alphabetical order

# 3. SLICING: Getting a specific part of a string
score_text = "SGPA:6.74"
just_score = score_text[5:]     # Slice from index 5 to the end
print(f"Final Friends: {trip_friends} | Current Score: {just_score}")