from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="inicio"), name="logout"),  # 👈 esto
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]