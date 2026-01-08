#the DATA we got
Marks= [39,98,40,86,59] 
 #we count fom marks from 1st place
Topper = Marks[0] 
for score in Marks:
    if score > Topper: 
        Topper=score #<--- TOPPER gets the new high score
print("The highest score in class: " +str(Topper))

# The Problem: You have 5 truck deliveries. You need to find which truck brought the heaviest load of bricks.
Delivery = [1000,2000,3000,48800,3739,48393]
Highest_delivery = Delivery[0]
for weight in Delivery:
    if weight > Highest_delivery:
        Highest_delivery=weight  #the highest weight will count we want weight not Highest delivery
print("The High weight delivery is: "+str(Highest_delivery))

# Example: Finding the Lowest SGPA
result=[6.7,6.5,8.7,5.0]
lowest = result[0]
for sgpa in result:
    if sgpa < lowest:
        lowest=sgpa
print("THE LOWEST SGPA IN CLASS IS :" +str(lowest))