from django.conf.urls import url

from spider import views as spiderviews

urlpatterns = [
    url(r'^$',spiderviews.spider),
    url(r'^jianshu/',spiderviews.spiderJanshu),
]
