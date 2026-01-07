Firends_sgpa = [6.4,7.7,8.5,5.6]
ready_count = 0
for sgpa in Firends_sgpa:
    # Condition: 7.0 or higher for AI/ML roles
    if sgpa >= 7 :
        # Command: Add 1 to our counter
        ready_count = ready_count +1 
        print(" Status :This Pepole are eligible For AI/ML job role  "+str(sgpa))
# The Final Result (Outside the loop so it only prints once)
print(" Total Freinds are eligible For AI/ML Job role  "+str(ready_count))