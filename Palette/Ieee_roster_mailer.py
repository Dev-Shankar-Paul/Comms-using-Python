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

app_spec_pass_1 = "rmtzkgjrizvzqdmy"
app_spec_pass_2 = "vjdmeugftvrrusje"
database = pd.read_csv('/home/dsp/PROJECTS/Comms-using-Python/Outreach Database(IEEE Roster) - Banglore.csv')

# Setting up the matrices where the data is stored
chairs = database.iloc[:, 1]
chairs_email = database.iloc[:, 2]

counselors = database.iloc[:, 4]
counselors_email = database.iloc[:, 5]

mail_status = database.iloc[:, 9]

# Printing the total of each matrix
print("Total number of chairs : ", len(chairs))
print("Total number of counselors : ", len(counselors))

# Configuring the mail 
from_address = input("Enter your email ID : ")
password = input('Enter your mail password : ')

msg_chair = MIMEMultipart()
msg_counselor = MIMEMultipart()

msg_chair['From'] = from_address
msg_counselor['From'] = from_address

msg_chair['Subject'] = "Join us for Palette'20"
msg_counselor['Subject'] = "Join us for Palette'20"

body_chair = """Hey, greetings from IEEE-VIT! hope you're safe and doing well,

We’re an IEEE student chapter based in VIT Vellore. We wanted to come up with an event to give designers a platform to show their talent to the world and to get their creative neurons to start firing.

On 22nd May we are hosting a one-of-a-kind design hack, Palette- 'Where your palette of ideas can meet the color palette'. We would be thrilled to have your fellow chapter members to participate in our event and further spread the word to other enthusiastic designers.

You can find more about us on our page and our website. 
https://palette.ieeevit.org/ 
And check out our Instagram page 
https://bit.ly/2T1Rpz8
"""
body_counselor = """Respected Sir/Ma’am,
Greetings from IEEE-VIT! hope you're safe and doing well,

We’re an IEEE student chapter based in VIT Vellore. We wanted to come up with an event to give designers a platform to show their talent to the world and to get their creative neurons to start firing.

On 22nd May we are hosting a one-of-a-kind design hack, Palette- 'Where your palette of ideas can meet the color palette'. We would be thrilled to have the student members of your chapter to participate in our event and further spread the word to other clubs and chapters on your campus.

You can find more about us on our page and our website. 
https://palette.ieeevit.org/ 
And check out our Instagram page 
https://bit.ly/2T1Rpz8
"""

msg_chair.attach(MIMEText(body_chair, 'plain'))
msg_counselor.attach(MIMEText(body_counselor, 'plain'))

# Adding the attachment
filename = 'Palette.jpg'
attachment = open(os.getcwd() + r'/' + filename, "rb")
p = MIMEBase('Application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % 
             filename)

msg_chair.attach(p)
msg_counselor.attach(p)

# Starting mail service and connecting to sender's mail
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()

smtpobj.login(from_address, password)

for i in range(47, len(chairs)):
    
    # First sending mail to chair
    if(chairs[i] != '-' and chairs_email[i] != '-' ):
        msg_chair['To'] = chairs_email[i]
        text = msg_chair.as_string()
        smtpobj.sendmail(from_address, chairs_email[i], text)
    else:
        print(chairs[i], " Could not be sent a mail!", '\ncheck index ',
              i+1)
        
    print("No. of chairs sent mail : ", i+1)
    
    # Next sending the same mail to counselor
    if(counselors[i] != '-' and counselors_email[i] != '-'):
        msg_counselor['To'] = counselors_email[i]
        text = msg_counselor.as_string()
        smtpobj.sendmail(from_address, counselors_email[i], text)
        
        # Marking the status of mail sent or not
        mail_status[i] = 'Sent'
    else:
        print(counselors[i], "could not be sent a mail!", "\ncheck index ",
              i+1)
        mail_status[i] = 'Not Sent'
        
    print("No. of counselors sent mail : ", i+1)
       
smtpobj.quit()
    


