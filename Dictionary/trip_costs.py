# created dictionary
trip_costs ={"Ticket": 1500,
"Food": 2500,
"Stays": 3000
}

# input for perticuler cost
cost=input(f"which cost you want to see ?(Ticket ,Food or Stays): ")

# print cost that user wanted
print(f"The Budget of {cost} is :{trip_costs[cost]} ")

# Added new  Dictionary
trip_costs["Shopping"] = 1000

# added the cost of Ticket and Food 
print(trip_costs["Ticket"] + trip_costs["Food"])

# Printed The Updated Dictionary
print("\nUpdated Dictionary Cost Cabinet:")
print(trip_costs)