import random as rand
import smtplib
import os


class SendMail():

    @staticmethod
    def send_email(title, message, email="vaporbirdo@gmail.com", smtp_domain="smtp.gmail.com"):
        my_email = "vaporbirdo@gmail.com"
        password = os.environ.get("EMAIL_PASS") 
        print(my_email)
        print(email)
        print(password)
        connection = smtplib.SMTP(smtp_domain)
        connection.starttls()
        connection.login(user=my_email, password=password)
        msg_to_send = (f"Subject:{title}\n\n" + message).encode("utf8")
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=msg_to_send)
        connection.close()
