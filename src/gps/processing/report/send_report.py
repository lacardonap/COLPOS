# Python code to illustrate Sending mail with attachments
# from your Gmail account

"""
References:
https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
https://www.tutorialspoint.com/send-mail-with-attachment-from-your-gmail-account-using-python
https://stackoverflow.com/a/27515883/9802768
"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging as log

from src.gps.config.general_config import EMAIL_SENDER_ADDRESS, EMAIL_SENDER_PASSWORD, SMTP_PORT, SMTP_SERVER


class SendReport:
    def __init__(self):
        self._mail_content = """
        Hola, acabas de recibir el reporte de procesamiento de datos GPS, el cual fue generado utilizado el servicio web de procesamiento de datos GPS COLPOS (versión 0.0.1)."""

    def send(self, receiver_address, report_path):

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = EMAIL_SENDER_ADDRESS
        message['To'] = receiver_address
        message['Subject'] = 'GPS Processing result'  # The subject line

        # The body and the attachments for the mail
        message.attach(MIMEText(self._mail_content, 'plain'))

        # open the file to be sent
        filename = os.path.basename(report_path)
        attachment = open(report_path, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        message.attach(p)

        # Create SMTP session for sending the mail
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # use gmail with port
        session.starttls()  # enable security
        session.login(EMAIL_SENDER_ADDRESS, EMAIL_SENDER_PASSWORD)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(EMAIL_SENDER_ADDRESS, receiver_address, text)
        session.quit()
        log.info('Mail Sent')
