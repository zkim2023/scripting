def assign_grade(score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    else:
        return "Grade F"

# Get user input
try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        print(assign_grade(score))
    else:
        print("Please enter a valid score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numerical score.")
