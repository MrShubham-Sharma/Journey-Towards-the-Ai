# lambda function 
# lambda function is a small anonymous function that can take any number of arguments, 
# but can only have one expression.
def add(x, y):
    # This is a regular function that adds two numbers
    return x + y
double = lambda x: x * 2
# This is a lambda function that doubles a number
print(double(5)) 
cube = lambda x: x ** 3
# This is a lambda function that cubes a number
print(cube(3))
square = lambda x: x ** 2
# This is a lambda function that squares a number
print(square(4))
# lambda function with multiple arguments
add = lambda x, y: x + y
# This is a lambda function that adds two numbers
print(add(5, 3))
subtract = lambda x, y: x - y   
# This is a lambda function that subtracts two numbers
print(subtract(10, 4))
multiply = lambda x, y: x * y
# This is a lambda function that multiplies two numbers
print(multiply(6, 7))
divide = lambda x, y: x / y
# This is a lambda function that divides two numbers
print(divide(20, 5))
# lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())
# lambda function with default arguments
power = lambda x, y=2: x ** y
# This is a lambda function that raises a number to the power of y, with a default value of 2 (squares the number if y is not provided)
print(power(5))
print(power(5, 3))
avg = lambda x,y: (x+y)/2
# This is a lambda function that calculates the average of two numbers
print(avg(10, 20))
print(avg(15, 25))