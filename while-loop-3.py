a = 'ajaz'
b = 'unknown'

firstname = input('')
secondname = input('')

while firstname != a or secondname != b:
    firstname = input('enter first name :')
    secondname = input('enter second name :')

    if firstname == a and secondname == b:
        print('Success')

    elif firstname == a and secondname != b:
        print ('Failed, Try Again !')
    elif firstname == ''and secondname == '':
        print('Error')

    else:
        print('Something is wrong')