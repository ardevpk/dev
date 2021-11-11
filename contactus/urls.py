from django.urls import path
from contactus import views

urlpatterns = [
    path('contactus/', views.index, name='contactus'),
    path('submitting/', views.submitting, name='submitting'),
    path('submit/', views.submit, name='submit'),
    path('sending/', views.sending, name='sending'),
    path('contact/', views.contact, name='contact')
]
