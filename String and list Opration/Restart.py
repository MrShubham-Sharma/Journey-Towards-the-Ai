# Topic: String Slicing & List Manipulation
location = "  mumbai road  "

# 1. Clean the string
clean_loc = location.strip().title()
# 2. Reverse it (The classic interview trick)
reversed_loc = clean_loc[::-1]

print(f"Original: {clean_loc}")
print(f"Reversed: {reversed_loc}")

# 3. Quick List Update
friends = ["Rohit", "Parth"]
friends.append("Shubham")
friends.sort()
print(f"Updated Friend List: {friends}")