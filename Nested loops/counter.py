# The "Building Material" Counter
floors = ["Floor 1", "Floor 2"]
rooms_per_floor = [1, 2, 3]

total_rooms = 0


# outer loop 
for floor in floors:

    # inner loop
    for room in rooms_per_floor:
        total_rooms = total_rooms + 1

# final total count
print(f"Total rooms counted: {total_rooms}")