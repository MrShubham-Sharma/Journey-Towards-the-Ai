# Break
numbers = list(range(0,100))
for number in numbers:
    if number > 20:
        break
    print(number)
while True:
    num =input("Enter The Number (q For Quite) :")
    # if we enter q it will quite loop
    if num =='q' :
        break
    print(num)

# continue
# we have to Skip 2 and 4
for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)

# Now We Have to Print 2,4,6,8
n=0
while n<10:
    n +=1
    if n%2  !=0:
        continue
    print(n)