# 'w' stands for WRITE. 
# WARNING: 'w' deletes everything in the file and starts fresh!
file = open("trip_list.txt", "w") 

file.write("Rohit\n") # \n moves the cursor to a new line
file.write("Parth\n")
file.write("Shubham\n")

file.close() # Always close the door!