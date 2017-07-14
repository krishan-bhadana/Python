"""
Practice Problem 1: 
AcadView is running an internship program in MRIU cmapus. Being a Computer Science student, your task is 
to help out the AcadView team in writing welcome emails for the students who have opted for this 
program. The program should take the first name, last name, gender, mobile number, email and amount 
paid as input and should display a welcome email for the student if he/she has paid the complete Fee, 
else display a message stating the remaining balance to be paid. The total fee is Rs. 2499.

Sample 

Example 1 :

Input: 
First Name : Puneet
Last Name : Gupta
Gender : Male
Mobile No. : 9958805478
Email : gupta.puneet0696@gmail.com
Amount Paid : 2499

Output :
To gupta.puneet0696@gmail.com
Mobile : 9958805478
Hi, Mr. Puneet Gupta!
Welcome to the AcadView internship program! We have successfully received the payment of Rs. 2499. 

Example 2:

Input:
First Name : Ankita
Last Name : Singh
Gender : Female
Mobile No. : 9976457821
Email : ankita.singh@gmail.com
Amount Paid : 1499

Output :
To ankita.singh@gmail.com
Mobile : 9976457821
Hi, Ms. Ankita Singh!
You have a remaining balance of Rs. 1000 to be paid. Please make the payment as soon as possible to enroll with us.

"""

#Code:

first_name = raw_input("Enter the first name: ")    # input from user
last_name = raw_input("Enter the last name: ")
gender = raw_input("Enter the gender: ")
mobile = raw_input("Enter the mobile number: ")
email = raw_input("Enter the email address: ")
amount_paid = int(raw_input("Enter the amount paid: "))

print "To:" + " " + email
print "Mobile:" + " " + mobile

if gender == "Male":  # to decide the salutation of the student
	salutation = "Mr."		  # Mr. for Male
else:
	salutation = "Ms."		  # Ms. for Female
print("Hi, " + salutation + " " + first_name + " " + last_name)   # string concatenation

if amount_paid == 2499:     # amount calculation
	print "Welcome to the AcadView internship program! We have successfully received the payment of Rs. 2499."
else:
	print "You have a remaining balance of Rs.", 2499 - amount_paid, "to be paid. Please make the payment as soon as possible to enroll with us."