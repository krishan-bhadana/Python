year=raw_input('Enter the year')
if (int(year)%100==0):
    if(int(year)%400==0):
        print('leap year')
    else:
        print('not a leap year')
elif(int(year)%4==0):
    print('leap year')
else:
    print('not leap year')