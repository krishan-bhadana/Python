'''
Practice Problem 5:

Puneet and Rohit are playing Game.
There are N coins in a pile. In each turn, a player can choose to remove one or two coins.The players keep alternating turns and whoever removes the last coin from the table wins.
Puneet always starts first. And the each player must make a move.
Note :
	Both players are playing optimally.

Input:
	5
	6

Output:
	Puneet
	Rohit							
'''

#CODE:

num_of_coins = int(raw_input('Enter the Number of Coins: '))

print ("Rohit" if num_of_coins%3==0 else "Puneet") # ternary Operator