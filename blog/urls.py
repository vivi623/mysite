from django.conf.urls import url

from blog import views as blogviews

urlpatterns = [
    url(r'^$',blogviews.index),
    url(r'^(?P<article_id>[0-9]+)/',blogviews.article),
]
