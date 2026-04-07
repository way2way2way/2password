#keep is simple stupid!!
import time
import sys
import getpass
import hashlib
super = 5
username = input('set username:')
password = getpass.getpass('set password:')
hash_object = hashlib.sha256(password.encode())
password = hash_object.hexdigest()
password2 = getpass.getpass('set 2password:')
hash_object = hashlib.sha256(password2.encode())
password2 = hash_object.hexdigest()
while True:
    loginusername = input('enter username:')
    logintry = getpass.getpass('enter password:')
    hash_object = hashlib.sha256( logintry.encode())
    logintry = hash_object.hexdigest()
    logintry2 = getpass.getpass('enter 2password:')
    hash_object = hashlib.sha256( logintry2.encode())
    logintry2 = hash_object.hexdigest()
    if password == logintry and password2 == logintry2 and username == loginusername:
        print('login successful!')
        sys.exit()
    else:
        time.sleep(super)
        super += super
        print('error username or password or 2password miss')
