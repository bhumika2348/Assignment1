

# Input: Percentage from the user
percentage = float(input("Enter your percentage: "))

# the grade using if-else ladder
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F (Fail)"

# Output: the grade
print("Your grade is: ",grade)
