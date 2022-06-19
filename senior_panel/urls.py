from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_panel, name='user_panel'),
    path('delete_picture/<int:picture_id>/', views.delete_picture, name='delete_picture'),
]
