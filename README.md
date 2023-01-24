# CELERY FORM

Example of using celery for backend task (submitting forms) and scheduled task.

## Run Celery and Redis no docker

Must start up celery using command:

```celery -A celery_form.celery worker --loglevel=info --pool=solo ``` 

```celery -A APP.celery worker --loglevel=info --pool=solo ``` 

for scheduled task must also run:

```celery -A celery_form.celery beat```

```celery -A APP.celery beat```

In settings.py include and start redis server (docker or redis)

``` CELERY_BROKER_URL = 'redis://localhost:6379' ```

launch docker compose file with  ```docker compose up```

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

2. create task.py with celery task in app. In this exmaple we have one for form submission and another for scheduled task

3. Within view send form data to task

    ``` debug_task.delay(data) ```

    Task will be sent to celery for execution


4. For scheduled task add folowing in settings:

```
CELERY_BEAT_SCHEDULE = {
      'add-every-30-seconds': {
        'task': 'home.tasks.say_hello',
        'schedule': 5.0,
        'args': (),
        'options': {
            'expires': 15.0,
        },
    },
}
```

4. In Production add following code to procfile to start celery workers:

    ``` worker: celery -A YOUR-PROJECT_NAME worker -l info -B ```

5. Make Docker Image for web application

6. Make docker compose file for all services

7. To run commands use:

``` docker exec -it container_id python manage.py createsuperuser ```
