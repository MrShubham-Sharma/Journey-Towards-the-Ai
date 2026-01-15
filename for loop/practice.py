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