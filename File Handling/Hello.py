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
with open("Hello.txt","a") as user_file:
    user_file.write("Hello Brother\n")

Hello = open("Hello.txt","r")
print(Hello.read())
Hello.close()

with open("Helllo.txt","w") as user_file:
    user_file.write("Hello Master Shubh\n")
    user_file.close()

Hello = open("Helllo.txt","r")
print(Hello.read())
Hello.close()
Hello.close()