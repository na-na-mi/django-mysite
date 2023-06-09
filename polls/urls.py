from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetData.index, name="index"),
    # path("index/", views.SalesAPIVIew.as_view, name='poll'),
]
