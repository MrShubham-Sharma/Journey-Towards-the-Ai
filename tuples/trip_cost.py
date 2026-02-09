def total_expenses(*costs):
    grand_total = sum(costs)
    return grand_total

# TEST IT with different numbers of items
day1 = total_expenses(500, 1200)
day2 = total_expenses(100, 450, 2000, 800, 150)

print(f"Day 1 Total: Rs.{day1}")
print(f"Day 2 Total: Rs.{day2}")