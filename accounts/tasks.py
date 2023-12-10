from django.core.mail import send_mail

def send_profile_creation_confirmation(email='alamin.csecu.bd@gmail.com'):
    send_mail(
        subject='Profile Creation Confirmation',
        message='Your Profile is Created Sucessfully. Please Update your profile.',
        from_email='spikesp1089@gmail.com',
        recipient_list=[email, 'mdalaminbijoy3@outlook.com'],
        # fail_silently=True
    )
