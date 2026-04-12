list1 = [1, 2, 3]
list2 = [4, 5, 6]
i = 0
j = 0
# Outer loop will run until i is less than the length of list1
while i < len(list1):
    # Inner loop will run until j is less than the length of list2
    while j < len(list2):
        print(list1[i], list2[j])
        j += 1
    print("Inner loop is completed for i =", list1[i])
    i += 1
    # Reset j to 0 for the next iteration of the outer loop
    j = 0