from django.urls import path
from p4 import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('portfolio-details/', views.ptdetails, name='pages'),
]
