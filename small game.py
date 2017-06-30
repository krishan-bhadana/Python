# give a number N the player must subtract 1,2 or 3 from N in order to make a number that is divisible by 4. the game will continue until any player is able to make such a number ,
# and the player doing so wins the game. prince is generous guy and he allows shubham to start first.
number=raw_input('Give the number to start the game : ')
flag=0
k=0
while(flag!=1):
    i=k%2
    if(i==0):
        name = 'Shubham'
        key=raw_input('.\n.\nyour turn '+name+' ,Subtract 1 or 2 or 3 from '+number+',make your choice : ')
    else:
        name = 'prince'
        key=raw_input('.\n.\nyour turn '+name+' ,Subtract 1 or 2 or 3 from '+number+',make your choice : ')
    number=int(number)
    number=number-int(key)
    if (number%4==0):
        print('\n.\n.\n!!! '+name+', You Won !!!')
        flag=1
    k=k+1
    number=str(number)