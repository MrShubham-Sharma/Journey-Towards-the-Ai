# lambda function 
# lambda function is a small anonymous function that can take any number of arguments, 
# but can only have one expression.
double = lambda x: x * 2
print(double(5)) 
cube = lambda x: x ** 3
print(cube(3))
square = lambda x: x ** 2
print(square(4))
# lambda function with multiple arguments
add = lambda x, y: x + y
print(add(5, 3))
subtract = lambda x, y: x - y   
print(subtract(10, 4))
multiply = lambda x, y: x * y
print(multiply(6, 7))
divide = lambda x, y: x / y
print(divide(20, 5))
# lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())
# lambda function with default arguments
power = lambda x, y=2: x ** y
print(power(5))
print(power(5, 3))
avg = lambda x,y: (x+y)/2
print(avg(10, 20))