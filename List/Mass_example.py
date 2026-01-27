# created an list 
friends_group = ["Rohit","Parth","Akash","Shagun","Pratik"]
print(friends_group[0])

# used the .remove() opraton
friends_group.remove("Shagun")

friends_group.append("Prashant")

# The 'in' operator checks if the name exists first
if "Shagun" in friends_group:
    friends_group.remove("Shagun")
    print("Shagun has been removed.")
else:
    print("Shagun was not in the list!")


friends_group.sort()

# use the .join for clen output
perfect_names = ",".join(friends_group)
print(f"{perfect_names} These are My Niphad's Friends")