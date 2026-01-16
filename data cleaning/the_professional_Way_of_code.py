bricks = ['Red', 'Black', 'Red', 'Red', 'Black', 'Black', 'Red']
while 'Black' in bricks:
    bricks.remove('Black')
    print(bricks)

bricks = ['Red', 'Black', 'Red', 'Red', 'Black', 'Black', 'Red']

# The Magic Sieve: "Keep the brick UNLESS it is Black"
clean_bricks = [b for b in bricks if b != 'Black']

print(clean_bricks)

