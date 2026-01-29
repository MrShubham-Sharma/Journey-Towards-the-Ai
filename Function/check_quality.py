# 1. 'def' means "Define a Machine"
# 'check_quality' is the name of the machine
# 'price' is the input (the material we put in)

def check_quality(price):
    if price >= 7000:
        return "Premium Quality"
    else:
        return "Local Quality"

# 2. Now we use (call) the machine
result = check_quality(8500)
print(f"This item is: {result}")

def calculate_avg(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return avg

# Now call it with your real data
my_scores = [5.67, 5.93, 5.61, 6.09, 6.74]
final_result = calculate_avg(my_scores)
print(f"My average is: {final_result:.2f}")