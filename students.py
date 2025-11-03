# Program to record marks of 3 students and determine pass/fail

NUM_STUDENTS = 3
NUM_SUBJECTS = 3

for i in range(NUM_STUDENTS):
    print(f"\n--- Enter details for Student {i+1} ---")
    name = input("Enter student's name: ")

    marks = []
    for j in range(NUM_SUBJECTS):
        mark = float(input(f"Enter mark for subject {j+1}: "))
        marks.append(mark)

    average = sum(marks) / NUM_SUBJECTS
    status = "Passed" if average >= 50 else "Failed"

    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Result: {status}")

    print("\n--- Program Finished ---")
