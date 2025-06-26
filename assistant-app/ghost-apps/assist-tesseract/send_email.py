
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:

    def send_email(subject, body):
        # Yahoo SMTP server credentials and settings
        yahoo_smtp_server = "smtp.mail.yahoo.com"
        yahoo_smtp_port = 465

        # Email and password for your Yahoo account
        yahoo_email = "j_kitsakis@yahoo.com"
        yahoo_password = "ezkmbmewffcftkeh"
        # Gmail address to send email to
        recipient_email = "jkitsakis@gmail.com"

        # Creating the MIME email message
        message = MIMEMultipart()
        message["From"] = yahoo_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            # Establishing a secure connection using SSL
            with smtplib.SMTP_SSL(yahoo_smtp_server, yahoo_smtp_port) as server:
                server.login(yahoo_email, yahoo_password)
                server.sendmail(yahoo_email, recipient_email, message.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
