from django.core.mail import send_mail
from celery import shared_task

@shared_task(bind=True)
def send_profile_creation_confirmation(self, email):
    send_mail(
        subject='Profile Creation Confirmation',
        message='Your Profile is Created Sucessfully. Please Update your profile.',
        from_email='spikesp1089@gmail.com',
        recipient_list=[email],
        # fail_silently=True
    )
    return 'EMAIL SENT'
