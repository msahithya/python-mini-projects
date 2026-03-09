name = input("Enter student name: ")

marks = []

for i in range(3):
    m = int(input("Enter mark: "))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

print("\nStudent:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Grade: D")
