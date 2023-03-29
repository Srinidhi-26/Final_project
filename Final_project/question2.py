test1 = float(input("Enter score for test 1: "))
test2 = float(input("Enter score for test 2: "))
test3 = float(input("Enter score for test 3: "))

average_score = (test1 + test2 + test3) / 3
#calculating the average score of all the 3 tests
# and storing it in the variable called average_score

if average_score >= 90:
    grade = "A"
elif 80 <= average_score < 90:
    grade = "B"
elif 70 <= average_score < 80:
    grade = "C"
elif 60 <= average_score < 70:
    grade = "D"
else:
    grade = "F"
# Assigning the grade based on the input given
# by the user for the all tests marks

print(" Average score is:", average_score)
print("Final grade is:", grade)
#printing the average score and the grade the given marks

