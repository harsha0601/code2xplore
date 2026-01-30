student_id = input("Enter student id: ")
email = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter Referral code: ")
count = 0
if (len(student_id) == 7 and student_id[0:3] == "CSE" and student_id[3] == "-" and student_id[4:].isdigit()):
    count += 1
if ("@" in email and "." in email and email[0] != "@" and email[-1] != "@" and email[-4:] == ".edu"):
    count += 1
if (len(password) >= 8 and password[0].isupper() and
        (password[0].isdigit() or
         password[1].isdigit() or
         password[2].isdigit() or
         password[3].isdigit() or
         password[4].isdigit() or
         password[5].isdigit() or
         password[6].isdigit() or
         password[7].isdigit())):
    count += 1
if (len(referral) == 6 and referral[0:3] == "REF" and referral[3:4].isdigit() and referral[5] == "@"):
    count += 1
if count == 4:
    print("APPROVED")
else:
    print("REJECTED")
