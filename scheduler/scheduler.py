from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from datetime import date
from django_apscheduler.models import DjangoJobExecution
import sys
from twilio.rest import Client

account_sid = 'ACe4458a38ffc43eb3b5dafd515a50f0f7'
auth_token = 'efcd9f6cff42f79df9d6ab4ceb63dfc8'
client = Client(account_sid, auth_token)


from service.models import StudentModel
from prestij.models import SettingsModel

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def deactivate_expired_accounts():
    today = date.today()

    students = StudentModel.objects.filter(
        status = "DE"
    )
    settings = SettingsModel.objects.first()
    for student in students:
        duration = today - student.payment_date
        if duration.days == 3:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=settings.student_message1,
                to='whatsapp:' + student.wp_number
            )
        elif duration.days == 0:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=settings.student_message2,
                to='whatsapp:' + student.wp_number
            )
        elif duration.days == -3:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=settings.student_message3,
                to='whatsapp:' + student.wp_number
            )

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(deactivate_expired_accounts, 'interval', hours=24, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)