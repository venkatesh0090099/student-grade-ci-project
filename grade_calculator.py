def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


# Display student result
total = calculate_total(80, 90, 70)
average = calculate_average(80, 90, 70)
grade = calculate_grade(average)

print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)