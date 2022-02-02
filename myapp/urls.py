from . import views
from django.urls import path

urlpatterns = [
    path('', views.retrive_all),
    path('add', views.add),
]
