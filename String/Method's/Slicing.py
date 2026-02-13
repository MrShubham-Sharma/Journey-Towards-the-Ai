#Sting Method
Name = "SHUBhAM"
print(Name[0:4])   #It Will Print SHUBH
print(Name[::-1])  #It Will Print MAHBUHS
print(Name[3:])    #It Will Print BHAM
print(Name[-3:])   #It will Print HAM

# Use Cases
print(Name.upper())          #It Will Print SHUBHAM
print(Name.lower())          #It Will Print shubham
print(Name.title())          #It Will Print Shubham
print(Name.capitalize())     #It Will Print Shubham
print(Name.swapcase())       #It Will Print shubHam

score = " SGPA:6.74 "
print(score[5:])                                  #It Will Print 6.74
print(score.strip())                              #It Will Print SGPA:6.74
print(score.lstrip())                             #It Will Print SGPA:6.74
print(score.rstrip())                             #It Will Print  SGPA:6.74
print(score.replace(" SGPA:6.74 ","SGPA:9.00"))   #It Will Print SGPA:9.00 It Will Replace

# Sting To List Opration
Friend = "Rohit,Parth"                   
Friend_list = Friend.split(",")          
print(Friend.split(","))                 #It Will Print ['ROhit','Parth']
  
new_string =" | ".join(Friend_list)      
print(new_string)                        #It Will Print ROhit | Parth

Final_string = ",".join(Friend_list)     
print(Final_string)                      #It Will Print Rohit,Parth 