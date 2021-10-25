from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pets all'),
    path('details/<int:pk>/', views.pet_details, name='pet details'),
    path('like/<int:pk>/', views.pet_likes, name='pet likes')
]
