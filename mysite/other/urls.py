from django.conf.urls import url

from . import views

urlpatterns = [
    # Change how we reference the new view.
    url(r'^now/$', views.ShowTimeView.as_view()),
]
