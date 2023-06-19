from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

User = get_user_model()

@receiver(post_save, sender=User)
def send_new_user_notification(sender, instance, created, **kwargs):
    if created and instance.role != 'pokupatel' and instance.is_active:
        subject = 'New User Registration'
        message = f'A new user with role {instance.role} has registered.'
        from_email = 'admin@salatik.com'
        admin_email = 'sharikov@gmail.com'  # адрес администратора
        # send_mail(subject, message, from_email, [admin_email])