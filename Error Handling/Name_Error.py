def smart_station(station, *costs):
    try:
        total = sum(costs)
        return f"Bill for {station} is: Rs.{total}"
    
    except TypeError:
        return "❌ Error: You can only add numbers, not words!"
        
    except Exception as e:
        # This is a 'Catch-All' net for any other weird errors
        return f"⚠️ Something else went wrong: {e}"

# TEST IT
print(smart_station("Mumbai Central", 500, "Free", 20))