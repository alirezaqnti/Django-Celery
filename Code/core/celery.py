import os
from celery import Celery
# because we used the same code base for configure django and celery in docker compose
# and we did not start django in celery we need to add the following line:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# with this we definin Celery app and now we can make some changes
app = Celery('Code')

# with this celery reads the celert settings in settings.py
# namespace defines the prefix name that Celery should look for in settings.py to ger its settings
app.config_from_object('django.conf:settings',namespace='CELERY')

# by using @app.task we are registering this task
# with celery so celery can find this task and then be ready to execute
# this task whenever it is requested
@app.task
def add_number():
    return


# we need a way to tell celery to look for tasks
# the following line will search within every app in INSTALLED_APP
# and get tasks from tasks.py files
app.autodiscover_tasks()
