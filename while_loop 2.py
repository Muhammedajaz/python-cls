user = 'ajaz'
password = '1234'

username = ''
passw = ''

while username != user or passw != password:
    username = input ('enter user name :')
    passw =input('enter password :')
    if username == user and passw == password:
        print ('login succes')

    elif username == user and passw != password:
        print (username ,'your password is incorrect')
    elif (username == "" and passw == ""):
        print('enter username and password')
    else :
        print('user name or password is wrong')









    

