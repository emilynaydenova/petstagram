from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pets all'),
    path('details/<int:pk>/', views.pet_details, name='pet details'),
    path('like/<int:pk>/', views.pet_likes, name='pet likes'),
    path('create/', views.pet_create, name='pet create'),
    path('edit/<int:pk>/',views.pet_edit, name='pet edit'),
    path('delete/<int:pk>/', views.pet_delete, name='pet delete'),
    path('comment/<int:pk>/',views.add_comment,name='add comment'),
]
