from flask import Flask, render_template, request
import smtplib

eapp = Flask(__name__)

@eapp.route('/')
def home():
    return render_template('index.html')

@eapp.route('/send_email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    receiver_email = request.form['receiver_email']
    subject = request.form['subject']
    message = request.form['message']

    try:
        # Establish SMTP connection
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            # Login to sender's email account
            smtp.login('your_email@gmail.com', 'your_password')

            # Create email message
            email_message = f'Subject: {subject}\n\n{message}'

            # Send email
            smtp.sendmail(sender_email, receiver_email, email_message)

        return render_template('result.html', result='Email sent successfully!')
    except Exception as e:
        return render_template('result.html', result=f'Error occurred while sending email: {str(e)}')

if __name__ == '__main__':
    eapp.run()
