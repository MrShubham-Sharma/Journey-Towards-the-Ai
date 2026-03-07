with open("internship_log.txt","a") as Robokart:
    try:
        Robokart.write("Mastering Math and Data Logic\n")
        print("log updated successfully")
    except Exception as e:
    # This catches ANY error (Permission, Disk Full, etc.)
        print(f"Error: {e}")