def create_student_record(name, sgpa, semester):
    record = {
        "Student_Name": name,
        "Current_SGPA": sgpa,
        "Sem": semester
    }
    return record

# Creating your record based on your Sem 5 results
shubham_data = create_student_record("Shubham", 6.74, 6)
print(shubham_data)