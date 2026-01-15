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


# --- ROOM 1: INPUT (The Materials) ---
# We create a list to store your historical data
my_sgpa = [5.67, 5.93, 5.79, 6.7]

# We start our 'sum' at 0 because we haven't added anything yet
total_sum_sgpa = 0

# We pick the first item as the 'King of the Hill' to start the comparison
highest_sgpa = my_sgpa[0]


# --- ROOM 2: PROCESS (The Work) ---
# The 'for' loop acts as a conveyor belt, picking up one SGPA at a time
for sgpa in my_sgpa:
    
    # 1. ADDING: We take the current sgpa and add it to our running total
    total_sum_sgpa = total_sum_sgpa + sgpa
    
    # 2. COMPARING: We ask if the current sgpa is bigger than our current record
    if sgpa > highest_sgpa:
        # If true, we update our record with the new higher value
        highest_sgpa = sgpa


# --- ROOM 3: OUTPUT (The Result) ---
# These are NOT indented, so they only run once after the loop finishes
print("Total My sgpa is :" + str(total_sum_sgpa))
print("MY HIGHEST SGPA IS :" + str(highest_sgpa))

# 1. INPUT (The Materials)
brick_prices = [12, 15, 10, 18]
total_cost = 0  # Starting at 0 because we haven't bought any bricks yet

# 2. PROCESS (The Work)
for x in brick_prices:
    # We take the price 'x' and add it to our bucket
    total_cost = total_cost + x 

# 3. OUTPUT (The Result)
# We print the final sum after the loop finishes scanning all prices
print("THE TOTAL COST OF BRICKS IS: " + str(total_cost))