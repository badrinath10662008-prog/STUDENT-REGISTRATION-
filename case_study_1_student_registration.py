# topic: Student Information Registration System
# Concepts: input/output, variables, basic data validation

print("=" * 55)
print("       STUDENT INFORMATION REGISTRATION SYSTEM")
print("=" * 55)

student_id = input("Enter Student ID: ").strip()
while not student_id:
    print("Student ID cannot be empty.")
    student_id = input("Enter Student ID: ").strip()

name = input("Enter Student Name: ").strip()
while not name.replace(" ", "").isalpha():
    print("Enter a valid name using letters only.")
    name = input("Enter Student Name: ").strip()

gender = input("Enter Gender (Male/Female/Other): ").strip().title()
while gender not in ("Male", "Female", "Other"):
    print("Please enter Male, Female, or Other.")
    gender = input("Enter Gender: ").strip().title()

dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
while len(dob) != 10 or dob[2] != "-" or dob[5] != "-" or not (
    dob[:2].isdigit() and dob[3:5].isdigit() and dob[6:].isdigit()
):
    print("Use the format DD-MM-YYYY.")
    dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()

mobile = input("Enter Mobile Number (10 digits): ").strip()
while len(mobile) != 10 or not mobile.isdigit():
    print("Mobile number must contain exactly 10 digits.")
    mobile = input("Enter Mobile Number (10 digits): ").strip()

email = input("Enter Email Address: ").strip()
while "@" not in email or "." not in email.split("@")[-1] or " " in email:
    print("Enter a valid email address.")
    email = input("Enter Email Address: ").strip()

branch = input("Enter Branch: ").strip()
while not branch:
    print("Branch cannot be empty.")
    branch = input("Enter Branch: ").strip()

while True:
    admission_year = input("Enter Admission Year (e.g. 2026): ").strip()
    if len(admission_year) == 4 and admission_year.isdigit():
        admission_year = int(admission_year)
        break
    print("Enter a valid four-digit year.")

print("\n" + "=" * 55)
print("             STUDENT REGISTRATION DETAILS")
print("=" * 55)
print(f"Student ID       : {student_id}")
print(f"Name             : {name}")
print(f"Gender           : {gender}")
print(f"Date of Birth    : {dob}")
print(f"Mobile Number    : {mobile}")
print(f"Email Address    : {email}")
print(f"Branch           : {branch}")
print(f"Admission Year   : {admission_year}")
print("=" * 55)
print("Student registration completed successfully!")
