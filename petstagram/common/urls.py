from django.urls import path

from common import views

urlpatterns = [
    path('', views.landing_page,name='landing'),
]