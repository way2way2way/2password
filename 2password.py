#keep it simple stupid!!
import time
import sys
import getpass
import hashlib
stoper = 5
def encryptpass(text):
    return hashlib.sha256(text.encode()).hexdigest()
username = input('set username:')
password = encryptpass(getpass.getpass('set password:'))
password2 = encryptpass(getpass.getpass('set 2password:'))
while True:
    loginusername = input('enter username:')
    logintry = encryptpass(getpass.getpass('enter password:'))
    logintry2 =  encryptpass(getpass.getpass('enter 2password:'))
    if password == logintry and password2 == logintry2 and username == loginusername:
        print('login successful!')
        sys.exit()
    else:
        time.sleep(stoper)
        stoper += stoper
        print('error username or password or 2password miss')
