import imp
from celery_form.celery import app
from django.http import HttpResponse, JsonResponse

from .forms import ProfileForm


@app.task(bind=True)
def debug_task(self, form):
    print('celery form')
    print(form)
    profile = ProfileForm(form)
    profile.save()
    return HttpResponse(status=200) 