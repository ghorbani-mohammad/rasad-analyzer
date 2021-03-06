from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analyzer_app.settings")

# TODO: redis port and ip and db must be dynamic
app = Celery("app")

# Optional configuration, see the application user guide.
app.conf.update(result_expires=7200)
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# if you want to purge works queue
app.control.purge()

MINUTE = 60

app.conf.beat_schedule = {
    "news_mongo_to_postgres": {
        "task": "news_mongo_to_postgres",
        "schedule": 5 * MINUTE,
    },
    "news_keyword_extraction": {
        "task": "news_keyword_extraction",
        "schedule": 20 * MINUTE,
    },
    "news_ner_extraction": {
        "task": "news_ner_extraction",
        "schedule": 10 * MINUTE,
    },
    "news_geo_extraction": {
        "task": "news_geo_extraction",
        "schedule": 25 * MINUTE,
    },
    "news_sentiment": {
        "task": "news_sentiment",
        "schedule": 35 * MINUTE,
    },
    "news_doc2vec": {
        "task": "news_doc2vec",
        "schedule": 5 * MINUTE,
    },
    "news_related": {
        "task": "news_related",
        "schedule": 10 * MINUTE,
    },
    "news_category": {
        "task": "news_category",
        "schedule": 20 * MINUTE,
    },
    "news_summary": {
        "task": "news_summary",
        "schedule": 15 * MINUTE,
    },
}
