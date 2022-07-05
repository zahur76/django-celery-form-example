# CELERY FORM

Example of using celery when submitting forms in django.

## Run Celery and Redis

Must start up celery using command:

```celery -A django_celery.celery worker --loglevel=info --pool=solo ``` 

In settings.py include and start redis server (docker or redis)

``` CELERY_BROKER_URL = 'redis://localhost:6379' ```

## Steps

1. Create celery.py file in startproject folder

    ``` from __future__ import absolute_import, unicode_literals

    import os

    from celery import Celery

    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_form.settings')

    app = Celery('django_celery')

    # Using a string here means the worker doesn't have to serialize
    # the configuration object to child processes.
    # - namespace='CELERY' means all celery-related configuration keys
    #   should have a `CELERY_` prefix.
    app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django app configs.
    app.autodiscover_tasks()```

2. create task.py with celery task in app

3. Within view send form data to task

    ``` debug_task.delay(data) ```

    Task will be sent to celery for execution

4. In Production add following code to procfile to start celery workers:

    ``` worker: celery -A YOUR-PROJECT_NAME worker -l info -B ```