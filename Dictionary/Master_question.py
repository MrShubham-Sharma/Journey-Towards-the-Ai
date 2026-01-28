# Add a new material to your dictionary called "Bricks", but instead of one price, 
# give it a List of two prices: [5000, 7000] (one for local quality, one for premium quality).
# Print the Premium price (the second item in the list) from the "Bricks" locker.

# Dictionary 
material = "Bricks"
print(f"the Price of The Bricks")

# price of the material 
Material_cost = [4000,7000]

# cost input
Cost = int(input(f"What is the Budegt of the {material} ? :"))

# id else for quality check
if Cost < 7000:
    print(f"the {material} is Local")
else:
    print(f"The {material} is primium")