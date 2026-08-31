a=int(input("Enter marks of DS"))
b=int(input("Enter marks of OS"))
c=int(input("Enter marks of AI"))
d=int(input("Enter marks of DELD"))
e=int(input("Enter marks of UHV"))

total=a+b+c+d+e
percentage=total/5
print("total marks:",total)
print("percentage:",percentage,"%")

if percentage >=90:
    print("Grade: 1st class")
elif percentage >=75:
    print("Grade: 2nd class")
elif percentage >=50:
    print("Grade: 3rd class")
else:
    print("The student is failed")
