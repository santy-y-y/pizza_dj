from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.register, name = 'registration')
]