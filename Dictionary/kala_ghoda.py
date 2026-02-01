# Function with a default 'entry_fee' of 0 (since many events are free)
def festival_expense(food, shopping, entry_fee=0):
    total = food + shopping + entry_fee
    return f"Total spent at Kala Ghoda: ₹{total}"

# Scenario: You spent 300 on Vada Pav/Tea and 500 on a souvenir
print(festival_expense(300, 500))