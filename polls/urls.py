from django.urls import path
from . import views
from .views import visualize_rules

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),

    path("test/", views.test, name="test"),
    path('visualize/', visualize_rules, name='visualize_rules'),
]
