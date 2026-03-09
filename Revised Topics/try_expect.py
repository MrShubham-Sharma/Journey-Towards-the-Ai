log_entry = "Revision Day 1: Mastering Math and Data Logic\n"

try:
    with open("internship_log.txt", "a") as Robokart_file:
        Robokart_file.write(log_entry)
    print("Log successfully saved to your Lenovo LOQ.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")