import random 
import string 
def crack_password(password):
 attempts = 0
 while True:
  guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
  attempts += 1
  if guess ==password:
   return attempts

password = input('Enter the password 10 craclk: ')

print('cracking password....')

attempts = crack_password(password)
print(attempts)