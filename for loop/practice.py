bag = [15,51,25,30,38]
for weight in bag :
    if weight >20 :
        print(f"the weigth of bag {weight} is good for supply")
    else:
        print(f"go back {weight} it's not enough come with more weight")

# while Loop
bag_loaded = 0
while bag_loaded <3:
    weight =int(input("How much weight bag have ?"))
    if weight >20:
        print("Success! Adding it to the truck.")
        bag_loaded= bag_loaded +1
    else:
        print("Too light! This bag stays behind.")
print("Truck is full. Ready to leave for the site!")


# You want to withdraw 500 rupees, but you only have 3 attempts to get the PIN right.
# the counter
attempt = 0

# the prosses
while attempt <3:

    # input from user 
    pin = int(input("enter your pin :"))
    if pin == 1234:

        print("you can withdraw the cash")
        # break for instant out from the loop
        break

    else:
        # count the attempt +1
        attempt = attempt +1

        # 3- will give out of the 0 count
        print(f"you remaining attempt is :{3-attempt}")   
print("your transaction is finish")