# Creating a variable
City ,Days,Budget ="Darjling",12,5000 
# print in morden way 
print(f"I'm Going to : {City} for {Days} Day's With budget of :{Budget} ")


# creating and variable and assigning them 
Workers ,material , limit = 26,"Cement",40

# now we have to print today work limit and material
print(f"Today our {Workers} Pick up {limit} of the {material} ")

Friends =["Parth "," Rohit ","Parin","Shreyansh","Deepak"]
friend1,friend2 ,*friend3 = Friends
# The Bucket: others is ['Shreyansh','Parin','Deepak'].
# The Glue: ", ".join(others) takes the words out and puts a , between them.
normal_names = ", ".join(friend3)
print(f"my best friends are {friend1}and{friend2 } other This are my Casual Friends {normal_names} ")