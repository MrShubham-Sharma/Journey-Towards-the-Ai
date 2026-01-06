# sgpa is variable Which assigned to reuqired sgpa 7.0
sgpa = 7.0 
# here was an input where we take from user
Sem_6_sgpa = float(input("Enter Your sgpa Of 6 Sem :"))
# here condition starts where it's equal or more than the eligible for job role 
if Sem_6_sgpa >= sgpa :
    print("Status : Your eligibal for Ai/Ml Job Role")
# if the grater than the 6.5 then user in safe zone
elif Sem_6_sgpa >= 6.5 :
    print("Status : Your in safe zone But GIve more Effort Next time")
# else where the condition ends where user need more efforts 
else:
    print("Status : Your Need TO Rise at least 6.5+")