from celery.task.schedules import crontab
from celery.decorators import periodic_task
from yahoo_app.yahoo_finance import shares_io

@periodic_task(run_every=(crontab(minute='*/1')), name="get_shares_informations", ignore_result=True)
def get_shares_informations():
    shares = shares_io()