#Copyright (C) 2026 2password
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
