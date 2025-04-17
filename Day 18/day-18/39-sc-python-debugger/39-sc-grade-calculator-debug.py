# grade_calculator.py

def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    avg = total / count
    return avg

def determine_grade(avg):
    breakpoint()      # <- the code execution stops here
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

grades = [85, 92, 78]
average = calculate_average(grades)
final_grade = determine_grade(average)

print(f"Average: {average}")
print(f"Final Grade: {final_grade}")
