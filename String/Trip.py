Trip_location=("Darjeeling","Gangtok","Siliguri")
print(Trip_location[1][::-1])
try:
    Trip_location[0]="sikkim"
except:
    print("You cannot change a Tuple!")
current_Friend =["Parth","Rohit"]
current_Friend.append("Shubham")
print(current_Friend)