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