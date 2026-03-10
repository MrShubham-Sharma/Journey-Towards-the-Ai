# Topic: Persistent Storage & Error Handling
update = "Revision session complete: Foundations are 100% restored.\n"

try:
    # 'a' mode appends data without deleting previous history
    with open("internship_log.txt", "a") as file_handle:
        file_handle.write(update)
    print("Log successfully saved to internship_log.txt")
except Exception as error:
    # Catches any issues with file permissions or missing folders
    print(f"Security Alert: Could not save file. Error: {error}")