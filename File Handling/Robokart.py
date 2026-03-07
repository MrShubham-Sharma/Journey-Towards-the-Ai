# Topic: File Handling with 'with' and Append mode
note = "Finished Robokart internship session - Back to AI/ML learning!"

# 'a' mode ensures we don't delete old data
with open("career_log.txt", "a") as file:
    file.write(note + "\n")

print("Note saved permanently to career_log.txt")