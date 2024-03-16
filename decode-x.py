import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres de connexion au serveur SMTP
smtp_server = 'smtp.example.com'
port = 587  # Port SMTP (587 est souvent utilisé pour le chiffrement TLS)

# Vos informations d'identification
sender_email = 'dodjokun178@gmail.com'
password = 'password178?'

# Destinataire
receiver_email = 'destinataire@example.com'

# Créer un message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sujet de l\'email'

# Corps du message
body = 'Contenu de l\'email.'
message.attach(MIMEText(body, 'plain'))

# Connexion au serveur SMTP
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Activer le chiffrement TLS
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
