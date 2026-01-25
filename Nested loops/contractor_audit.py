# total count reset
grend_total = 0 

# for loop for names
for friend in ["Rohit","Bharat","Sidhhant"]:
    
    # try for condition of input
    try:
        ammount = int((input(f"How much Rs. {friend} Save today ? :")))
        grend_total += ammount
    
    # it will give error if input was not filed or uexpected input
    except ValueError:
        print(f" Error!: You entered text. Skipping {friend}'s entry for now.")

# print the total savings 
print(f"All Friends total Rs. {grend_total} was Saved ")