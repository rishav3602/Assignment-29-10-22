#7 . write a function which will be able to send a mail to anyone 


import smtplib , ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "rishavkumar7294@gmail.com"  # Enter your address
receiver_email = "rishavseth362002@gmail.com"  # Enter receiver address
password = 'iceeezbugcvtamme'
message = """this is my message from python code in my live class"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)