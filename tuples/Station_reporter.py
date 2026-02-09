def station_reporter(station, *other_costs):
    try:
        # Summing the vacuum bag
        total = sum(other_costs)
        return f"Station: {station} | Total Spent: Rs.{total}"
    except TypeError:
        return " Logic Error: One of your station costs is not a number!"

# Commit this logic
print(station_reporter("Mumbai Central", 500, 20, 15, 25))