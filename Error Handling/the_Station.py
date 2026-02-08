def smart_station(station, *costs):
    try:
        total = sum(costs)
        return f"Bill for {station} is: Rs.{total}"
    except TypeError:
        # What should the safety net say?
        return "Error: You Enter the Wrong Input Try Again "

# TEST IT with a mistake
print(smart_station("Mumbai Central", 500, "Free", 20))