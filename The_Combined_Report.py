# --- ZONE 1: PREPARATION ---
# We set up our empty buckets before the trucks arrive.
site_costs = [1200, 4500, 900, 2100]

total_sum = 0          # Bucket for adding all money
highest_cost = site_costs[0] # Bucket for the King of the Hill

# --- ZONE 2: THE WORK (The Loop) ---
for x in site_costs:
    # Task A: Add to the total sum
    total_sum = total_sum + x
    
    # Task B: Check if we found a new Highest Cost
    if x > highest_cost:
        highest_cost = x

# --- ZONE 3: THE RESULT ---
# We print everything AFTER the loop is finished (no indentation).
print("Total Money Spent: " + str(total_sum))
print("The Most Expensive Item: " + str(highest_cost))

my_sgpa = [5.67, 5.93, 5.79, 6.7]
total_sum_sgpa = 0
highest_sgpa = my_sgpa[0]
for sgpa in my_sgpa:
    total_sum_sgpa = total_sum_sgpa + sgpa
    if sgpa> highest_sgpa:
        highest_sgpa= sgpa
print("Toatal My sgpa is :"+str(total_sum_sgpa))
print("MY HIGHEST SGPA IS :"+str(highest_sgpa))