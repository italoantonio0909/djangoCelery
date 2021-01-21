from celery import shared_task


@shared_task
def send_mail():
    return 'Envío de emails'
