import smtplib
# simple mail transfer protocol library

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# object for server
# provide domain server and port number - alternatively port 465
# if doesn't work - firewall or antivirus
smtp_object.ehlo()
# greets the server and establish connection