def print_receipt(**items):
    # 'items' is now a Dictionary (The Filing Cabinet)
    print("--- YOUR RECEIPT ---")
    
    for name, price in items.items():
        print(f"{name}: Rs.{price}")
    
    total = sum(items.values())
    print(f"-------------------")
    print(f"GRAND TOTAL: Rs.{total}")

# THE TRIGGER: Look how we give names to the numbers!
print_receipt(Chai=20, Vada_Pav=15, Ticket=500, Water=20)