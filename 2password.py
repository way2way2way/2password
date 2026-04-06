#keep is simple stupid!!
username = input('set username:')
password = input('set password:')
password2 = input('set 2password:')
loginusername = input('enter username:')
logintry = input('enter password:')
logintry2 = input('enter 2password:')
if password == logintry and password2 == logintry2 and username == loginusername:
    print('login successful!')
else:
    print('error')