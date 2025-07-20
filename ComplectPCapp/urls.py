# ComplectPCapp/urls.py
from django.urls import path
from . import views

app_name = 'ComplectPCapp'

urlpatterns = [
    path('', views.home, name='home'),  # http://127.0.0.1:8000/
    path('submit/', views.submit_config, name='submit_config'),  # http://127.0.0.1:8000/submit/
    path('success/', views.success_page, name='success_page'),  # http://127.0.0.1:8000/success/
]