name = input("Enter full name: ")
email = input("Enter email ID: ")
Number = input("Enter your Mobile No.: ")
age=int(input("Enter age: "))
count=0
if name[0] != ' ' and name[-1] != ' ' and '' in name:
    count+=1
if email.count('@') == 1 and email.count('.') == 1 and email[0] != '@':
    count+=1
if len(Number) == 10 and Number.isdigit() and Number[0] != '0':
    print("Valid Mobile No.")
    count+=1
if 18<=age<=60:
    count+=1
if count==4:
    print("User profile is VALID")
else:
    print("User profile is NOT VALID")