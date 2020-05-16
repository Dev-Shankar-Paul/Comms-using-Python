#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:39:15 2020

@author: dsp
"""
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

database = pd.read_csv('/home/dsp/PROJECTS/Comms-using-Python/Roster_Test - Sheet1.csv')

# Setting up the matrices where the data is stored
chairs = database.iloc[:, 1]
chairs_email = database.iloc[:, 2]

counselors = database.iloc[:, 4]
counselors_email = database.iloc[:, 5]

mail_status = database.iloc[:, 9]

# Configuring the mail 
from_address = input("Enter your email ID : ")
password = input('Enter your mail password : ')

msg = MIMEMultipart()
msg['From'] = from_address
msg['Subject'] = input('Enter the subject of the mail : ')
body = input("Enter the body of the mail : ")
msg.attach(MIMEText(body, 'plain'))

# Adding the attachment
filename = 'Coronavirus.jpg'
attachment = open(os.getcwd() + r'/' + filename, "rb")
p = MIMEBase('Application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % 
             filename)
msg.attach(p)

# Starting mail service and connecting to sender's mail
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()

smtpobj.login(from_address, password)

for i in range(0, len(chairs)):
    
    # First sending mail to chair
    msg['To'] = chairs_email[i]
    text = msg.as_string()
    smtpobj.sendmail(from_address, chairs_email[i], text)
    
    # Next sending the same mail to counselor
    msg['To'] = counselors_email[i]
    text = msg.as_string()
    smtpobj.sendmail(from_address, counselors_email[i], text)
    
smtpobj.quit()
    


