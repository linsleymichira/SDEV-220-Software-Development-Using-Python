"""
Name: Linsley Michira
Description:
This program accepts student names and GPAs and determines whether
each student qualifies for the Dean's List or the Honor Roll.
The program continues to process student records until the user
enters 'ZZZ' as the last name.
"""

# Start processing student records
while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    # Sentinel value to end the loop
    if last_name.upper() == "ZZZ":
        print("Exiting program.")
        break

    first_name = input("Enter student's first name: ")

    # Accept GPA as a float
    gpa = float(input("Enter student's GPA: "))

    # Check Dean's List qualification
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")

    # Check Honor Roll qualification
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")

    else:
        print(f"{first_name} {last_name} did not qualify for honors.")

    print()  # Blank line for readability
