#USE GMAIL TO NOTIFY YOU WHEN THE ITEM HAS BEEN BOUGHT
#Add this to bottom of the bot.py if you want to use

import smtplib, ssl
from email.message import EmailMessage
from time import time, ctime, sleep


context = ssl.create_default_context()

time = str(ctime(time()))   #GET DATE AND TIME

msg = EmailMessage()
text = "Acquired a GPU at the following time: "
msg.set_content(str(text)+time+". \n"+link)    #ATTACHES LINK TO THE ITEM YOU BOUGHT

msg['Subject'] = 'Bought GPU'
msg['From'] = ""   #ENTER YOUR EMAIL HERE
msg['To'] = notifEmail

with smtplib.SMTP_SSL("smtp.gmail.com", "465", context=context) as server:
  server.login("1", "2")  #REPLACE 1 WITH YOUR EMAIL ADDRESS, REPLACE 2 WITH YOUR PASSWORD
  server.send_message(msg)
  
print("Email has been sent")
