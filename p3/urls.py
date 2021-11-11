from django.urls import path
from p3 import views

urlpatterns = [
    path("", views.index, name='home'),
]
