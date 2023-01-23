import imp
from celery_form.celery import app
from django.http import HttpResponse
from celery import shared_task

from .forms import ProfileForm


@app.task(bind=True)
def debug_task(self, form):
    print('celery form')
    print(form)
    profile = ProfileForm(form)
    profile.save()
    return HttpResponse(status=200) 


@shared_task
def say_hello():
    print("hello")
    return HttpResponse(status=200) 