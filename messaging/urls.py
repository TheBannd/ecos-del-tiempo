from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", lambda request: redirect("inbox")),

    path("inbox/", views.inbox, name="inbox"),
    path("send/<int:user_id>/", views.send_message, name="send_message"),
    path("conversation/<int:user_id>/", views.conversation, name="conversation"),
]