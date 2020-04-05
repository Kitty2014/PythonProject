import os

import smtplib

email_address=os.environ.get("email_user")
email_password=os.environ.get("email_pass")

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login(email_address,email_password)

	subject="Hello Welcome to Python"

	body="I love to learn Pyhton"

	msg=f"Subject:{subject}\n\n{body}"

	smtp.sendmail(email_address,"hello@gmail.com",msg)

