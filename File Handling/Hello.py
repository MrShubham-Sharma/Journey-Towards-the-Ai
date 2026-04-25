# Writing To The File
# w will create a new file if it does not exist and if it exist it will overwrite the content of the file
# write() method is used to write the content to the file
User = open("Hello.txt","w")
User.write("Hello Master\n")
User.write("Welcome To Python Programming\n")
# close() method is used to close the file
User.close()

# Reading The File
# r is used to read the file and read() method is used to read the content of the file
with open("Hello.txt", "r") as user_file:
    # read() method will read the entire content of the file and return it as a string
    content = user_file.read()
    # print() function is used to print the content of the file
    print(content)

# Appending To The File
# a is used to append the content to the file and if the file does not exist it will create a new file
with open("Hello.txt","a") as user_file:
    # write() method is used to write the content to the file and it will append the content to the file
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