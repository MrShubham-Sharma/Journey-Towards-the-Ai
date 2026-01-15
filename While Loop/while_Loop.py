# 1. INPUT (The Material)
counter = 1

# 2. PROCESS (The Work)
# "As long as counter is less than or equal to 5..."
while counter <= 5:
    print(f"Looping... Count is {counter}")
    
    # CRITICAL STEP: We must change the counter 
    # otherwise it will loop forever (Infinite Loop)!
    counter = counter + 1

# 3. OUTPUT (The Result)
print("The loop has finished!")



# Taking an user input for while loop 
days_left = 5

# start while loop where the count is over 
while days_left >0:

    # now it will be print cunting the days until Darjeeling ! 
    print(f"Counting down: {days_left} days until Darjeeling!")

    # the days_left=days_left -1 will decrece the days 
    days_left=days_left-1
    
# the final output 
print("Time to pack! We are leaving for Darjeeling!")


