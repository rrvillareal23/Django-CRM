from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("installer_dashboard/", views.installer_dashboard, name='installer_dashboard'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
    path("record/<int:pk>", views.customer_record, name='customer_record'),
    path("delete_record/<int:pk>", views.delete_record, name='delete_record'),
    path("add_record/", views.add_record, name='add_record'),
    path("update_record/<int:pk>", views.update_record, name='update_record'),
    path('record/<int:pk>/add_note/', views.add_note, name='add_note'),
    path('record/<int:pk>/add_note/', views.add_note, name='add_note'),


]