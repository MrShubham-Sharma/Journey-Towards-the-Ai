# A LIST of friends (We can add or remove people)
friends_list = ["Shubham", "Bharat", "Sidhhant"]
friends_list[1] = "Roommate" # This WORKS
print(f"List: {friends_list}")

# A TUPLE of fixed trip locations (These won't change!)
locations_tuple = ("Mumbai", "Howrah", "NJP", "Darjeeling")

# TRY TO CHANGE IT (This will CRASH)
# locations_tuple[1] = "Varanasi" 
# Python will say: 'tuple' object does not support item assignment