from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("rooms/", views.room_list, name="rooms"),
    path("rooms/add/", views.room_create, name="room_create"),
    path("rooms/<int:pk>/edit/", views.room_update, name="room_edit"),
    path("rooms/<int:pk>/delete/", views.room_delete, name="room_delete"),
    path("guests/", views.guest_list, name="guests"),
    path("guests/add/", views.guest_create, name="guest_create"),
    path("guests/<int:pk>/edit/", views.guest_update, name="guest_edit"),
    path("guests/<int:pk>/delete/", views.guest_delete, name="guest_delete"),
]
