with open("shubh.txt","w") as My_file: 
    My_file.write("Welcome Back Master\n")

with open("shubh.txt","r") as My_file:
    content = My_file.read()
    print(content)

# readline()
f = open ("shubh.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)