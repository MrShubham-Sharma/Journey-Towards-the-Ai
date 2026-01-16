# the input initialization
Bricks = ['Red','Black','Red','Red','Black','Black','Red']

# While loop for the Bricks 
while 'Black' in Bricks:
    print("The Bad Quality Of Brick Found! We Removed It ")
    
    # remove.('black') removes the bad brick and clean data 
    Bricks.remove('Black')

# the final output
print(f"The God Quality Bricks are {Bricks}")