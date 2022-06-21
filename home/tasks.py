import imp
from celery_form.celery import app
from django.http import HttpResponse, JsonResponse

from .forms import ProfileForm


@app.task(bind=True)
def debug_task(self, form):
    print(form)
    profile = ProfileForm(form)
    profile.save()
    HttpResponse(status=200) 