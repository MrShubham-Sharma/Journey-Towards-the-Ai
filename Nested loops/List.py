list1 = [1, 2, 3]
list2 = [4, 5, 6]
# i will take value from list1 and j will take value from list2
for i in list1:
    # the inner loop will run for each value of i and j will take value from list2
    # Once the inner loop is completed it will go to the next value of i and repeat the process
    for j in list2:
        print(i, j)