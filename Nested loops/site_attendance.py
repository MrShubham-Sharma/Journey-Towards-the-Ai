# OUTER LOOP: The Days
for day in [1, 2, 3]:
    print(f"--- 📅 Day {day} Starting ---")
    
    # INNER LOOP: The Shifts
    for shift in ["Morning", "Evening"]:
        # Action: Ask how many workers were present
        count = input(f"Enter worker count for Day {day}, {shift} shift: ")
        print(f"Logged: Day {day}, {shift} = {count} workers")
        
    print(f"--- ✅ Day {day} Finished ---\n")

print("Attendance for the whole week is complete!")