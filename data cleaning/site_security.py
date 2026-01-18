# Day 10: Multi-Condition Loop Control
people = ["Worker", "Worker", "VIP", "Worker", "Intruder", "Worker"]

print("--- Starting Site Entry Log ---")

for person in people:
    if person == "Intruder":
        print(" SECURITY BREACH! Intrusive person found. Locking all gates.")
        break  # STOP everything immediately
        
    if person == "Worker":
        continue  # SKIP the print for workers to keep the log clean
        
    if person == "VIP":
        print(f" Welcome, {person}! We have been expecting you.")

print("--- Log Process Ended ---")