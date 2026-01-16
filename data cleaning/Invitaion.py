friends = ["Rohit", "Omkar", "Shagun", "Parth"]
for name in friends:
    if name == 'Omkar':
        print("Skipping Omkar...")
        continue
    else:
        print(f"Sending invitation to: {name}")