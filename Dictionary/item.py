darjeeling_savings = {
    "Shubham": 4500,
    "Parth": 3000,
    "Rohit": 5000
}

print("Darjeeling Savings Report ")

# .items() gives you BOTH the Name (Key) and the Amount (Value) at once!
for name, amount in darjeeling_savings.items():
    print(f"{name} has saved ₹{amount}")