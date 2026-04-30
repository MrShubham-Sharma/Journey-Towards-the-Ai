# Topic: Lambda Functions for Arithmetic and Logic

# 1. Scaling: Doubling and Cubing
double = lambda x: x * 2
cube = lambda x: x ** 3

# 2. Advanced: Power with a default argument (Squares by default)
power = lambda x, y=2: x ** y

# 3. Logic: Average calculation
avg = lambda x, y: (x + y) / 2

print(f"Double 5: {double(5)} | Cube 3: {cube(3)}")
print(f"Power (5^3): {power(5, 3)} | Default (5^2): {power(5)}")
print(f"Average of 10 & 20: {avg(10, 20)}")