'''
Practice Problem 4:

You are given a string S, which only contains the letters "a" and "b". Your task is to remove adjacent elements which are same.
That is, you have to find the string with no two adjacent elements that are same.

example 
Input:
aaabbb

Output:
ab 

---------

Input:
aabb

Output:
ab

'''

#Code:

# Input string
s = raw_input()

# Let final string be p
p = "" 

# traverse the string element one by one
for char in s:
	# if (p is empty simply add that char) or (if p last element(p[-1]) is not equal to char)
	if p=='' or p[-1] != char :  
		p+=char
print p