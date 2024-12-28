import smtplib
import imghdr
from email.message import EmailMessage

SENDER= "p.nikul6403@gmail.com"
PASSWORD="meta tgmp ludf lrge"
RECEIVER = "p.nikul6403@gmail.com"

def send_email(image_path):
    print("send email started")
    email_message= EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just show a new customer!")

    with open(image_path, "rb")as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER,RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email ended")

if __name__ == "__main__":
    send_email(image_path="images/20.png")
