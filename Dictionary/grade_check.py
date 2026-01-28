# create an dictionary and assign value
my_grades = {
    "Sem 4": 6.09,
    "Sem 5": 6.74,
    "Python": "O"
}
# check is used for input
check = input("Which grade do you want to see? (Sem 4, Sem 5, or Python): ")

# Instead of hardcoding "Sem 4", use the 'check' variable!
print(f"Your grade for {check} is: {my_grades[check]}")

# this will add sem 3 grade
my_grades["Sem 3"] = 5.79
print("\nUpdated Grade Cabinet:")
print(my_grades)