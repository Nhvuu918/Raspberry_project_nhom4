import smtplib
from email.mime.text import MIMEText
import subprocess

ip = subprocess.getoutput("hostname -I").split()[0]

sender = "thaiminhtam6102005@gmail.com"
password = "hzip bubq ucug qipl"

receiver = "thaiminhtam6102005@gmail.com"

msg = MIMEText(f"Current Raspberry Pi IP: {ip}")
msg["Subject"] = "Raspberry Pi Booted"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent!")
