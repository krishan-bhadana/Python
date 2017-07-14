"""
Practice Problem 2:
Leap year. Let's write the same old program that we have been doing since the first time all of us 
learned to code. Your task is to write a program which takes a Year as the input and output 
if it is leap or not.

Example:

Input: 2012

Output:
2012 is a leap year!

Input: 
2015

Output:
2015 is not a leap year!
"""

# Solution

year = int(raw_input("Enter the year: "))   # Getting the input
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):   # condition or leap year
	print("%d is a Leap Year!" %year)
	# print (str(year) + " " + is a Leap Year!")
else:
	print("%d is Not the Leap Year!" %year)