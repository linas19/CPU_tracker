import smtplib
import psutil
import time
print("Welcome!!! This program automatically tracks the usage of CPU and if percentage \nfalls bellow asigned value sends e-mail notifying about it")
print("Enter CPU percentage to track: ")
target_percentage = input()
print("Enter your e-mail: ")
target_mail = input()
# Check CPU status
while True:
	x = psutil.cpu_percent(interval=3)
	if x < int(target_percentage):
		print("CPU bellow designated value")
		content = 'simulation finished'
		break
	elif x > int(target_percentage):
		print("Above given value")
# Start SMTP server and send mail
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('', '')
mail.sendmail('', target_mail, content)
mail.close()
