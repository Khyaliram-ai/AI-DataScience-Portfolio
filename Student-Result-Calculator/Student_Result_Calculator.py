student = {
    "name": "Rahul",
    "marks": [80, 75, 90]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

average = calculate_average(student["marks"])

print(f"Student: {student['name']}")
print(f"Average: {average:.2f}")

if average >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")