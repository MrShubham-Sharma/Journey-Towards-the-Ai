sagp_score =[5.67, 5.93, 5.61, 6.09, 6.74]
sagp_score.sort(reverse=True)
# 1. Get the total of all scores
total_sum = sum(sagp_score)

# 2. Divide by the number of semesters
average_cgpa = total_sum / len(sagp_score)

# 3. Print the result
print(f"My current Aggregate CGPA is: {average_cgpa:.2f}")

highest = max(sagp_score)
print(f"My best performance was: {highest}") # Will print 6.74