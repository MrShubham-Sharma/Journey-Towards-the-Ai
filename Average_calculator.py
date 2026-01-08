# Average Calculator
load = [23,49,34,54,67,69]
total_sum = 0
count =0
for x in load:
    total_sum = total_sum + x 
    count = count +1
average = total_sum/count
print("The average delivery weight is: " + str(average))