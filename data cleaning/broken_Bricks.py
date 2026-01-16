Bricks = ['Red','Black','Red','Red','Black','Black','Red']
while 'Black' in Bricks:
    print("The Bad Quality Of Brick Found! We Removed It ")
    Bricks.remove('Black')
print(f"The God Quality Bricks are {Bricks}")