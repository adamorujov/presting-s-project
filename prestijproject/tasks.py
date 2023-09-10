# from celery import shared_task

from service.models import StudentModel
import pywhatkit

# @shared_task
# def send_wp_notifications_to_students():
#     students = StudentModel.objects.filter(
#         status = "DE"
#     )
#     for student in students:
#         pywhatkit.sendwhatmsg(
#             phone_no="+944554732292",
#             message="Salam",
#             time_hour=22,
#             time_min=31
#         )
#     return "Messages sent!"

# send_wp_notifications_to_students.delay()

import schedule
import time

def send_wp_notifications_to_students():
    students = StudentModel.objects.filter(
        status = "DE"
    )
    for student in students:
        pywhatkit.sendwhatmsg(
            phone_no="+944554732292",
            message="Salam",
            time_hour=22,
            time_min=31
        )
    return "Messages sent!"

schedule.every(2).minutes.do(send_wp_notifications_to_students)

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)