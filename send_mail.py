import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '6b1fe6b65a23ed'
    password = '832accf19e2b89'
    message = f"<h3>New feedback submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li>" \
        f"<li>Rating: {rating}</li>" \
        f"<li>Comments: {comments}</li>" \
        f"</ul>"
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())