# the Data of student name 
for students in ["Omkar", "Shagun"]:

# take the student name from list from outer loop 
    print(f"the name of Student is :{students} ")

    # the inner loop which have subject 
    for subjects in ["Math", "Python"]:

        # the score input of student's subject
        score = input(f"Enter {students}'s marks {subjects}: ")

        # conformation of record of score and student 
        print(f"The Recorded {subjects}= {score}: ")

# final output
print("\n All grades are logged in the system! ")