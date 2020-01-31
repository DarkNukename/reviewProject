from celery.task import periodic_task
from celery.schedules import crontab

import requests

from .models import AppDataBase
from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist


@periodic_task(run_every = crontab(minute = '*/1'), name = 'app_task')
def app_task():

    A_URL = "http://127.0.0.1:8000/api/vacancies/"

    id_list = []
 
    response = requests.get(A_URL)
    vacancies = response.json()
    print(vacancies)

    my_base = AppDataBase.objects.all()
    n = my_base.count()

    for i in range(0, n):
        id_list.append(my_base[i].uuid)
    print(id_list)

    for vacancy in vacancies:
        try:
            rec = AppDataBase.objects.get(pk = vacancy['uuid'])
            rec.state = "ACTIVE"
            rec.save()

            uuid_index = id_list.index(vacancy['uuid'])
            id_list.pop(uuid_index)

        except ObjectDoesNotExist:

            rec = AppDataBase()
            rec.uuid = vacancy['uuid']
            rec.title = vacancy['title']
            rec.state = "ACTIVE"
            rec.owner = vacancy['owner']
            rec.save()
    
    if id_list:
        for uuid in id_list:
            rec = AppDataBase.objects.get(pk = uuid)
            rec.state = "ARCHIVE"
            rec.save()
