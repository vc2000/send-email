import smtplib 
import config  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


msg = MIMEMultipart()
msg["From"] = config.config["me"]
msg["To"] = config.config["email_send_to"]
msg["subject"] = "Venus's first email"
body = "Hi , Thank you for reading my first email"

                            #can be html 
msg.attach(MIMEText(body,"plain"))
text = msg.as_string()


                            #SMTP     #port number
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
# security 
server.starttls()

server.login(config.config["me"], config.config["password"])
server.ehlo()

                #you        #target
server.sendmail(config.config["me"],config.config["email_send_to"], text )

server.quit()




