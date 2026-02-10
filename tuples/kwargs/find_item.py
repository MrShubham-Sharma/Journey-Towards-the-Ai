def find_item(target_item, **all_expenses):
    # This loop goes through the logbook looking for one specific thing
    for item_name, price in all_expenses.items():
        if item_name.lower() == target_item.lower():
            return f"Found it! {item_name} cost Rs.{price}."
    
    return f"Sorry, {target_item} was not found in your expenses."

search = find_item("Train", Hotel=3000, Train=1500, Food=800)
print(search)