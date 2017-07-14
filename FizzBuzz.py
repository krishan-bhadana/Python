'''
Practice Problem 5:

Fizz Buzz!

N = integer number

print "fizz" when N is multiple of 3

print "buzz" when N is multiple of 5

print "fizzbuzz" when N is multiple of  3 and 5

print back the number if none of the above cases satisfy

'''


#CODE:

n = int(raw_input("Enter the number: ")) # input value
s = "" # empty string
 
if n%3 == 0 :
	s += 'Fizz'

if n%5 == 0:
	s += 'Buzz'

print (n if s=='' else s) # ternary Operator in python
