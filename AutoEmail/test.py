import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "code.dev.test0714"
reciever_email = "parekh.samarth@gmail.com"
password = "" # removed for security purposes
message = "Hello World!"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)
