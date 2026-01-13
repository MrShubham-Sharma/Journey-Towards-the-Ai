# --- ROOM 1: INPUT (The Setup) ---
# The 'Source of Truth' - the correct password.
correct_pin = "1234"

# An empty variable to store whatever the user types.
user_input = " "

# Our strike counter to track how many times they fail.
attempt = 0


# --- ROOM 2: PROCESS (The Logic Gate) ---
# The loop runs ONLY if the PIN is wrong AND attempts are less than 3.
while user_input != correct_pin and attempt < 3:
    
    # We ask for the PIN and show the current attempt number.
    # We use 'attempt + 1' so the user sees 1/3 instead of 0/3.
    user_input = input(f"Enter the PIN (attempt {attempt + 1}/3): ")
    
    # CRITICAL: We add 1 to the counter so the loop eventually stops.
    attempt = attempt + 1


# --- ROOM 3: OUTPUT (The Final Decision) ---
# Once the loop ends, we check WHY it stopped.
if user_input == correct_pin:
    # If the user typed the right PIN before 3 tries.
    print("Access Granted and welcome back!")
else :
    # If the loop stopped because 'attempt < 3' became False.
    print("Access Denied. System is locked.")