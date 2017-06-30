first_name=raw_input('First name : ')
last_ktname=raw_input('Last name : ')
Gender=raw_input('Gender : ')
Mobile=raw_input('Mobile No. : ')
Email=raw_input('Email : ')
amount_paid=raw_input('Amount paid : ')
amount_paid=int(amount_paid)
if (Gender=='male'):
    salutation='Mr. '
else:
    salutation='Ms. '
print('\n\n\n\nTo '+Email+'\nMobile : '+Mobile+'\nHi, '+salutation+first_name+' '+last_ktname+'!\nWelcome to the Acadview internship program!')
if (amount_paid<2499):
    print('your due amount is ')
    print(2499-amount_paid)
else:
    print('We have sucessfully received your payment of Rs. 2499')
