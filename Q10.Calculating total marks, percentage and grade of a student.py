#marks_of_student:subject_wise
maths=float(input("enter marks obtained in maths: "))
science=float(input("enter marks obtained in science: "))
social_science=float(input("enter marks obtained in social science: "))

#calculating_total_marks
total_marks= maths+science+social_science
print("total marks obtained by student: ", total_marks)

#calculating_percentage
percentage= total_marks/3
print("percentage obtained by student: ", percentage)

#finding_grade
if percentage>=80:
    print("Grade A is obtained by student")
elif percentage>=70 and percentage<80:
    print("Grade B is obtained by student")
elif percentage>=60 and percentage<70:
    print("Grade C is obtained by student")
elif percentage>=40 and percentage<60:
    print("Grade D is obtained by student")
elif percentage<40:
    print("Grade E is obtained by student")
