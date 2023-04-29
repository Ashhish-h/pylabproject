# OTP Generator:
# One-time Passwords (OTP) is a password that is valid for only one login session or
# transaction in a computer or a digital device. Now a days OTP’s are used in almost every service like
# Internet Banking, online transactions, etc. They are generally combination of 4 or 6 numeric digits or
# a 6-digit alphanumeric. 



import random
def generate(n):
    if n==1:
        return str(random.random())[-4:]
    elif n==2:
        return str(random.random())[-6:]
    else:
        l = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choices(l,k=6))
print('Welcome to the OTP generator\nDue to multiple choices we are bound to ask what kind of otp you want to generate\n')
print('The options are:-\n1.4 digit\n2.6 digit\n3.6 Digit alphanumeric')
n = int(input())
out = generate(n)
print(out)
