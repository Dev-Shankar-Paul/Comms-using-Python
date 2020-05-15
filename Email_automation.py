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





