# Writing To The File
User = open("Hello.txt","w")
User.write("Hello Master\n")
User.write("Welcome To Python Programming\n")
User.close()

# Reading The File
with open("Hello.txt", "r") as user_file:
    content = user_file.read()
    print(content)

# Appending To The File
with open("Hello.txt", "a") as user_file:
    user_file.write("Have A Nice Day\n")