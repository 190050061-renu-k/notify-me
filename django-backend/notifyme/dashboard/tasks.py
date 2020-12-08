from __future__ import absolute_import, unicode_literals
import pytz
from datetime import datetime

from celery import shared_task
from pyfcm import FCMNotification
from .models import Deadline


@shared_task
def send_notifications():
    for deadline in Deadline.objects.all():
        notify.delay(deadline.id)


@shared_task
def notify(id):
    deadline = Deadline.objects.get(id=id)
    if deadline.start_date<=datetime.now().replace(tzinfo=pytz.utc)<=deadline.end_date:
        pushservice = FCMNotification(
            api_key="AAAA-VpvPgs:APA91bFN6tcNosEz81mDxZEgwjb3KkL-_Oc_dxU_u9SDmGDWNGRozy-7-B_rKD59rURmeaLMRA0C8hn5gUtV3puCkCwHWMuNlBf31Dk9BJVokG-qlHbA2PfYAVVAsgNNky7JSRIgrL4b")
        course = deadline.course
        students = course.students.all()
        reg_tokens = list(student.registration_token for student in students)
        return pushservice.notify_multiple_devices(registration_ids=reg_tokens, message_body=deadline.message,
                                                   low_priority=not deadline.hard)
