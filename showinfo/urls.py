from django.conf.urls import url

from showinfo import views as showinfoviews

urlpatterns = [
    url(r'^index/',showinfoviews.index),
    url(r'^genmat1/',showinfoviews.genmat1),
    url(r'^genmat2/',showinfoviews.genmat2),
]
