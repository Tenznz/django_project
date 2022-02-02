from . import views
from django.urls import path

urlpatterns = [
    path('', views.retrive_all),
    path('add', views.add),
    path('read/<int:id>', views.get_person),

]
