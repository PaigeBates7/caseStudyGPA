#Paige Bates
#08/29/2024
#caseStudyGPA
#This app will accept students names and GPAs, it will test if the student qualifies 
#for either the Dean's List or the Honor Roll list. 

studentLastName = (input("Enter students last name or ZZZ to quit:"))
if studentLastName == "ZZZ":
    quit
else:
    studentFirstName = (input("Enter Student's First Name:"))
    GPA = float(input("Enter Student's GPA"))
    if GPA >= 3.5:
        print("Student Has Made The Dean's List")
    else:
       if GPA >= 3.25:
        print("Student Has Made Honor Roll")
