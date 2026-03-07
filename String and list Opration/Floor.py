# Topic: Sets (Uniqueness) & Floor Division
# Removing duplicates from a list of materials
audit_items = ["Cement", "Sand", "Bricks", "Cement", "Sand"]
unique_audit = set(audit_items)

# Engineering Math: How many full tickets for Darjeeling?
budget = 12000
ticket_price = 1650

full_tickets = budget // ticket_price  # Floor Division
leftover_cash = budget % ticket_price  # Modulus (Remainder)

print(f"Unique Items: {unique_audit}")
print(f"Full Tickets: {full_tickets} | Remaining: Rs.{leftover_cash}")