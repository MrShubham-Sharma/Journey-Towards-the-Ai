import random
def surprise_cost():
    Number = random.randint(10, 100)
    return Number
random_number = surprise_cost()
print(f"Your Random Number is :{random_number}")