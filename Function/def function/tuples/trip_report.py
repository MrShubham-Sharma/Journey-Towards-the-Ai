def trip_report(destination, *expenses):
    total = sum(expenses)
    return f"Trip to {destination} cost Rs.{total}"

# TEST IT
# Notice 'Darjeeling' goes to destination, and the numbers go to *expenses
print(trip_report("Darjeeling", 1500, 3000, 2000))