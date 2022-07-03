from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_panel, name='user_panel'),
    path('admin', views.admin_panel, name='admin_panel'),
    path('delete_picture/<int:picture_id>/', views.delete_picture, name='delete_picture'),
    path('add_calendar_entry/', views.add_calendar_entry, name='add_calendar_entry'),
    path('add_header_entry/', views.add_header_entry, name='add_header_entry'),
    path('delete_calendar_entry/<int:entry_id>/', views.delete_calendar_entry, name='delete_calendar_entry'),
    path('delete_header_entry/<int:entry_id>/', views.delete_header_entry, name='delete_header_entry'),
    path('change_user_info/', views.change_user_info, name='change_user_info'),
]
