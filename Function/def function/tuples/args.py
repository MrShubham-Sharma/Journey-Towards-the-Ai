def pack_for_trip(*items):
    print(f"You have packed {len(items)} items!")
    for item in items:
        print(f"- {item}")

# Now look! I can give it 2 items or 5 items, and it won't crash.
pack_for_trip("Shoes", "Camera")
print("-" * 20)
pack_for_trip("Jacket", "Charger", "Medicine", "Soap", "Map")