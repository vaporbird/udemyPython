#y ZAQ!xsw2##
#g zaq1xsw2## 

import smtplib

my_email = "vaporbirdo@gmail.com"
password = "pldlvuagdhmuehkk"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(from_addr = my_email, to_addrs = "vaporbirdo@yahoo.com", msg = "Subject:This is a test message\n\nHello MF")
connection.close()

