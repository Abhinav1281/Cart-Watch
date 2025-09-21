import smtplib
from email.mime.text import MIMEText
import yaml

email_config_file = "email_config.yaml"

with open(email_config_file, 'r') as file:
        config = yaml.safe_load(file)

for email in config['email']:
    from_email = email["user_email"]
    password = email["password"]
    smtp_server = email["smtp_server"]
    smtp_port = email["smtp_port"]
    login = from_email
    to_email = from_email  # Sending to self; modify as needed
            
def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        server.sendmail(from_email, [to_email], msg.as_string())