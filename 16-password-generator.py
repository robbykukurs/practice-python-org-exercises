#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#
#
#
#
#
#This is a simple radom password generator
import random
password = []
for i in range(10):
    a = random.choice('abcdefghijklmnopqrstuvwxyz0123456789-$%£@!?><')
    password.append(a)
#at this stage the list looks like: ['?', 'l', '3', 'b', '?', '-', '9', 'a', '2']
#we need to join the items together as per below syntax
final = "".join(password)
print(final)
