def calculator(a, b, operation):
    if operation == "add":
        return a + b  # Directly putting the result on the conveyor belt
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        # Instead of just printing, we return the error message
        return f"invalid {operation} please enter valid operation"
print(f"the brain of Computer")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (add, sub, mul, div): ").lower()
final_answer = calculator(num1, num2, op)
print(f"Result: {final_answer}")