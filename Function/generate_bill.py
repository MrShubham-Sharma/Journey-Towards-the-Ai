def generate_bill(item_name, raw_price):
    tax = raw_price * 0.05
    total = raw_price + tax
    return f" the total for {item_name} is RS.{total:.2f}"
print(generate_bill("Glass",500))
print(generate_bill("Sand",1000))

def generate_bill(item_name, raw_price):
    tax = raw_price * 0.05
    total = raw_price + tax
    return f"The total for {item_name} is ₹{total:.2f}"


print(generate_bill("Cement", 450))
print(generate_bill("Tiles", 1000))