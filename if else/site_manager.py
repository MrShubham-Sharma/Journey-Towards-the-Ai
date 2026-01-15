# it's a assigned value for requirement for user count
required_bricks = 10000
# We use int() because input() always takes text, but we need a number to compare
Current_bricks = int(input("Enter the number of bricks currently at the site:"))
# if we have actual bricks value's are geater than our requirement then condition satisfy  
if required_bricks < Current_bricks:
    print("Status: Stock is Sufficient you can work for Extra")
# elif the stock is Equal sufficient then we required can work with cureent bricks
elif required_bricks == Current_bricks:
    print("Status: Stock is Sufficient we required More Bricks In Future")
# else where the condition stops 
else:
    print("Status: Stock is Not sufficient We will Stop Work in som Time ")