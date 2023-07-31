def calculate_gpa(grade):
    if grade >= 90:
        return 4.0
    elif 80 <= grade < 90:
        return 3.7
    elif 75 <= grade < 80:
        return 3.3
    elif 70 <= grade < 75:
        return 3.0
    elif 65 <= grade < 70:
        return 2.7
    elif 60 <= grade < 65:
        return 2.3
    elif 55 <= grade < 60:
        return 2.0
    elif 50 <= grade < 55:
        return 1.7
    elif 45 <= grade < 50:
        return 1.3
    elif 40 <= grade < 45:
        return 1.0
    else:
        return 0.0

def calculate_cgpa(grades, credit_hours):
    total_credit_points = sum(grade * credit_hour for grade, credit_hour in zip(grades, credit_hours))
    total_credit_hours = sum(credit_hours)

    if total_credit_hours == 0:
        return 0

    cgpa = total_credit_points / total_credit_hours
    return cgpa

def main():
    num_courses = int(input("Enter the number of courses: "))
    grades = []
    credit_hours = []

    for i in range(num_courses):
        grade = float(input(f"Enter the grade for course {i + 1}: "))
        credit_hour = int(input(f"Enter the credit hours for course {i + 1}: "))
        grades.append(calculate_gpa(grade))
        credit_hours.append(credit_hour)

    cgpa = calculate_cgpa(grades, credit_hours)
    print(f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    main()
