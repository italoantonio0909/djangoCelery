from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tareas programadas
app.conf.beat_schedule = {
    'send-email-every-20': {
        'task': 'notification.tasks.send_mail',
        'schedule': 20
    }
}


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Petición: {self.request!r}')
