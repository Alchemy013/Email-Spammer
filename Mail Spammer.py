import smtplib as s
server = s.SMTP_SSL("smtp.gmail.com",465)
server.login("Your_email_id_here@gmail.com","Your_mail_pass_here")
text = """\
Your
Text
Here
"""
a="Email_id_here@gmail.com"
for i in range(1):
    server.sendmail("Your_email_id_here@gmail.com",a,text)
server.quit()
