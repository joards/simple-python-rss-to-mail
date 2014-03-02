
# code inspired by: http://cagewebdev.com/index.php/raspberry-pi-sending-emails-on-boot/

import smtplib
import socket
from email.mime.text import MIMEText
# Change to your own account information


def sendTingiMaile(mail_body, emne_tekst):
    print(emne_tekst)
    print(mail_body)

def sendTingiMail(mail_body, emne_tekst):
    to = 'email@sendes.her'                             # skift desse verdiene
    gmail_user = 'brukernavn@gmail.com'                 #
    gmail_password = 'passord'                          # 
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)    
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)

    msg = MIMEText(mail_body, _charset='utf-8')
    msg['Subject'] = emne_tekst
    msg['From'] = gmail_user
    msg['To'] = to   
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

if __name__ == '__main__':
    sendTingiMail("ny test av mailsendin", "python scriptet funke... fremdeles")
