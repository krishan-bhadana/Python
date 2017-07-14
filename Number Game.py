"""
Practice Problem 3:

Let's play a game today!
Prince and Shubham from your geek a bored of sitting at the back seat, so they decided to play a game.
The game was as follows - Given a number N the player must subtract 1, 2 or 3 from N in order to make 
a number that is divisible by 4. The game will continue until any player is able to make such a number, 
and the player doing so wins the game. 

Prince is a generous guy and he allows Shubham to start first. 

Your classmate Dhananjay now wishes to predict who is going to win the game. Your task is to help him 
out in predicting the winner of the game by writing a Python program. 

The program should take a number N as the input and output the name of the winner of the game.
 
Example:

Input: 6

Output: Shubham

"""

#Code:

N = int(raw_input("Enter the number: "))
if N % 4 == 0:   # the player has to make a move, so if it is divisible by 4 prince will win
	print "Prince" 
else:
	print "Shubham" 