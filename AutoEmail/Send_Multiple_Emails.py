import csv, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "parekh.samarth@gmail.com"
password = "heyThere@123"
context = ssl.create_default_context()
message = MIMEMultipart("alternative")
message["Subject"] = "School Clothing"
message["From"] = sender_email
text = "I just wanted to write to you personally because I have heard good things about your campus and school and I am interested. I am a 10th grade student from Edison, New Jersey, and I wanted to see if you had any t-shirts or paraphernalia available so I could represent your school! I am interested in majoring in computer science, with a minor in business and I am very interested in your school; I feel like I would definitely shine there. If you have any t-shirts size Adult-Small, pennants, or such I would appreciate it greatly! My address is: 1601 Deerfield Drive, Edison New Jersey, 08820. Please email me back if you would like to confirm your clothing delivery. Thank you so much! Sincerely, Samarth Parekh"

part1 = MIMEText(text, "plain")

message.attach(part1)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    with open("emails.csv") as file:
        reader = csv.reader(file)
        for email in reader:
            server.sendmail(sender_email, email[:450], message.as_string())
