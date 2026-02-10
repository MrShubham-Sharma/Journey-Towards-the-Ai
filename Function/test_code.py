def check_site_budget(site_name, budget, **expenses):
    print(f"--- Audit for {site_name} ---")
    
    actual_spent = sum(expenses.values())
    
    if actual_spent > budget:
        diff = actual_spent - budget
        return f" Over Budget by Rs.{diff}! (Spent: {actual_spent})"
    else:
        remaining = budget - actual_spent
        return f" Under Budget! Rs.{remaining} left. (Spent: {actual_spent})"

status = check_site_budget("Niphad Project", 10000, Cement=4000, Sand=2000, Labor=5000)
print(status)