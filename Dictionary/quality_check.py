# 1. We define the threshold in a dictionary
quality_thresholds = {"Bricks": 7000, "Cement": 500}

# 2. We ask the user just ONCE
material = "Bricks"
cost = int(input(f"What is the budget for {material}? : "))

# 3. We use the dictionary to make the decision
if cost < quality_thresholds[material]:
    print(f"The {material} is Local quality.")
else:
    print(f"The {material} is Premium quality.")