import random
import qrcode

def gen_passward(char):
	l='abcdefghijklmnopqrstuvwxyz'
	u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	no='12345678901234567890'
	symbol='!@#$%^&*(){}:"<>;'
	virtual=l+u+no+symbol
	password=''.join(random.sample(virtual,char))
	print(password)
	return password

def qr(password):
	name=input('digit name password : ')
	img = qrcode.make(password)
	img.save(name+'.jpg')

def run():
	length = int (input('Enter the Length of password : '))
	password = gen_passward(length)
	print('your new password is :', password)
	qr(password)
	print('the password was save as QR Code img')

run()

