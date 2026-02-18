# open() will file my_file.txt 
# w stands for for Write. It tells Python: "I want to write something new. 
# If this file already exists, delete everything inside and let me start fresh
my_file=open("Owner.txt", "w")

# write() stands for Writing/Overrding 
my_file.write("The Owneris Shubham\n")
my_file.write("The Goal Is to Become an Ai/ML Engineer\n")
my_file.close()