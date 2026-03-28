# Topic: Additive and Subtractive Assignment
stock_on_hand = 500

# 1. Incrementing: New shipment arrives
stock_on_hand += 150  # Equivalent to: stock_on_hand = stock_on_hand + 150

# 2. Decrementing: Materials used today
stock_on_hand -= 80   # Equivalent to: stock_on_hand = stock_on_hand - 80

# 3. Simple counter increment
current_day = 29
current_day += 1

print(f"Total Stock Available: {stock_on_hand}")
print(f"Moving to Day: {current_day}")

# Topic: Multiplicative and Floor Division Assignment
material_price = 2000.0

# 1. Scaling: Applying an 18% tax increase
material_price *= 1.18  

# 2. Remainder: Calculating leftover budget after purchases
my_wallet = 10000
unit_cost = 1500
my_wallet %= unit_cost # Updates wallet to just the remainder (1000)

# 3. Floor Division: Dividing total units into 3 equal site zones
total_bricks = 5000
total_bricks //= 3

print(f"Updated Price (with Tax): ₹{material_price}")
print(f"Leftover Wallet Balance: ₹{my_wallet}")
print(f"Bricks per Zone: {total_bricks}")