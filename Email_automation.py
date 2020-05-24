#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:41:54 2020

@author: dsp
"""

# The calssic email. Just a subject and a short body with some text 
"""
import smtplib

smtpObject = smtplib.SMTP('smtp.gmail.com', 587)
smtpObject.ehlo()

smtpObject.starttls()

email_id = input("Enter your email ID : ")
password = input("Enter your password : ")

send_to = input("Enter the email ID of the receiver : ")

smtpObject.login(email_id, password)

smtpObject.sendmail(email_id, send_to,
                    'Subject: Email using python\n'+
                    'Hello. This is a test mail. It\'s awesome'+
                    ' isn\'t it?\nSigned\nDSP')

smtpObject.quit()
"""

# Levelling up. Sending attachments in an email 
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from_address = input("Enter your email ID : ")
to_address = input("Enter the email id of the recipient : ")

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = input('Enter the subject of the mail : ')

body = input("Enter the body of the mail : ")

msg.attach(MIMEText(body, 'plain'))

filename = 'Coronavirus.jpg'
attachment = open(os.getcwd() + r'/' + filename, "rb")

p = MIMEBase('Application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % 
             filename)

msg.attach(p)

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()

password = input("Enter your mail password : ")

smtpobj.login(from_address, password)
text = msg.as_string()
smtpobj.sendmail(from_address, to_address, text)
smtpobj.quit()
"""


