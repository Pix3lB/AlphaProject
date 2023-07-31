from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("GamePage", views.GamePage, name="GamePage"),
    path("signup", views.signup, name="signup"),
    path("", views.Logout, name="Logout"),
    path("Profile",views.profile,name="profile"),
    path("Profile/edit",views.editprofile,name="editprofile"),
    path("players",views.players,name="players"),
]