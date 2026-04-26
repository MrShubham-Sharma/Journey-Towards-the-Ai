with open("Marks.txt","r") as Students_marks :
    i =0
    while True:
        i+=1
        line = Students_marks.readline()
        if not line:
            break
        M1= int(line.split(",")[0])
        M2= int(line.split(",")[1])
        M3= int(line.split(",")[2])
        print(f"Marks of Shubham {i} Maths is :{M1*2}\n")
        print(f"Marks of Sidhhant {i} Science is :{M2*2}\n")
        print(f"Marks of Bharat {i} OPPS is :{M3*2}\n")

        print(line)