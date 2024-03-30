#send email with change password link
from django.core.mail import send_mail
from django.conf import settings

def send_change_password_email(email, token):
    subject = 'Change Password'
    message = f'Click the link below to change your password:\n\nhttp://'
    email_from = settings.EMAIL_HOST 
    
    send_mail(subject, message, email_from, [email])

def send_registration_email(email):
    subject = 'Successful Registration'
    message = f'You have successfully registered with us'
    email_from = settings.EMAIL_HOST 
    
    #probably have a variable in the settings by name of the particular hospital and append it to the message
    send_mail(subject, message, email_from, [email])