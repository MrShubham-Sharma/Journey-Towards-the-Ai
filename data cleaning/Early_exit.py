# Initialization Input 
materials = ["Cement", "Sand", "Steel", "Rust", "Bricks"]

# using for loop for entry of data 
for item in materials :

    # if the item have the Rust then use the break for instat puase 
    if item =="Rust":
        print("🚨 DANGER: Rust found! Stopping inspection.")
        break

    # else it will print until the Rust is not found
    else:
        print(f"Item {item} is safe. Continuing...")