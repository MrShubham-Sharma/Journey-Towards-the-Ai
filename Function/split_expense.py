# use def for define machine 
def split_expense(stays_cost, food_cost, friends_count=4):
    
    # total cost count logic
    total = stays_cost + food_cost

    # spliting logic
    share = total / friends_count

    # return values 
    return f"Each person owes: Rs.{share:.2f}"

# final print data
print(split_expense(30000,40000))