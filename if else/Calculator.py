# First input from user
Num1 = float(input("Enter First Number : "))
# oprators which perform oprations
Opration =input("Enter oprator(+,*,-,/) : ")
# Second input from user 
Num2 = float(input("Enter Second Number : "))
# the logic for calculator
if Opration == "+":
    print("Result :" +str(Num1 + Num2))
elif Opration == "-":
    print("Result :" +str(Num1 - Num2))
elif Opration == "*" :
    print("Result :" +str(Num1 * Num2))
elif Opration == "/":
    # Safety Check: You can't divide by zero!
    if Num2 != 0:
        print("Result :" +str(Num1 / Num2))
    else:
        print("The Number is not Divisible")
else:
    print("invalide Oprator")