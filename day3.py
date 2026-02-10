person = input("Enter who is entering the marks: ")
if person.lower() == "chitti":
    v = "!"
else:
    v = "*"
n = int(input("Enter No.of Students: "))
student = [0] * n
for i in range(n):
    student[i] = int(input("Enter Marks of Student-" + str(i+1) + ": "))
vc = 0
fc = 0
for i in range(n):
    if student[i] < 0 or student[i] > 100:
        print("Student-", i+1, " Marks = ", student[i], " --> Invalid ", v, sep="")
    elif student[i] >= 90:
        vc = vc + 1
        print("Student-", i+1, " Marks = ", student[i], " --> Excellent ", v, sep="")
    elif student[i] >= 75:
        vc = vc + 1
        print("Student-", i+1, " Marks = ", student[i], " --> Very Good ", v, sep="")
    elif student[i] >= 60:
        vc = vc + 1
        print("Student-", i+1, " Marks = ", student[i], " --> Good ", v, sep="")
    elif student[i] >= 40:
        vc = vc + 1
        print("Student-", i+1, " Marks = ", student[i], " --> Average ", v, sep="")
    else:
        vc = vc + 1
        fc = fc + 1
        print("Student-", i+1, " Marks = ", student[i], " --> Fail ", v, v, sep="")
print("Total Valid Students: ", vc, " ", v, sep="")
print("Total Failed Students: ", fc, " ", v, sep="")
