#created the list for firends 
Friends_group = ["Parth","Rohit","Shubham","Pratik"]

# the name initializer
print(Friends_group[0])

# .append() works as if we forget the somithing in program to add 
Friends_group.append("Kartik")

# for this clean_name = ", ".join(Friends_group) works for clean output
clean_names = ", ".join(Friends_group)

# finally print the output with adding forgoted item with clean output
print(f"This {clean_names} are Coming to Darjling")