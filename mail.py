import os
import smtplib

SENDER_EMAIL = os.environ.get('PLANT_MAIL') #"plant.alert21@gmail.com"
EMAIL_PW = os.environ.get('PLANT_PW')
rec_mail = "chris_boesener@gmx.net"


def sending_mail(reciver=rec_mail, body="Das ist die Default-nachricht."):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(SENDER_EMAIL,EMAIL_PW)
        print("Login success")

        subject = "Plant Alert!"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(SENDER_EMAIL, reciver,msg)

        print("email has been sent to ", reciver)
