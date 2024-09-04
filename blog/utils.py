from django.core.mail import send_mail
from django.conf import settings


def send_notification_email(article_title):
    subject = "Поздравляем! Ваша статья достигла 100 просмотров"
    massage = f'Здравствуйте! Ваша статья "{article_title}" достигла 100 просмотров. Спасибо за ваши внимание!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [from_email]

    send_mail(subject, massage, from_email, recipient_list)
