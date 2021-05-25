n = int(input())

student_grades = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for key, value in student_grades.items():
    avg = sum(value) / len(value)
    value_as_string = ' '.join(f"{x:.2f}" for x in value)
    print(f"{key} -> {value_as_string} (avg: {avg:.2f})")

