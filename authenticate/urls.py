from django.urls import path
from authenticate import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("register/", views.register_user, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.del_user, name='delete'),
]
