from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('count', views.get_count_client, name='count')
]
