def split_bill(total, friends):
    try :

        Slpited_bill = total / friends
        return f" the Total bill is :{Slpited_bill}"
    
    except TypeError:
        return f"You Enter The Wrong Inpuut Try Again"

    except ZeroDivisionError:
        return f"you Can not Divide By The Zero Count"
    
print(split_bill(20000 ,4))          #Works 
print(split_bill(10000,"Shubham"))   #catches type error
print(split_bill(10000, 0))          # Catches Zero Error