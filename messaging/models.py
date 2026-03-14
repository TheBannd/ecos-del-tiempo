from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver}"
    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, "messaging/inbox.html", {"messages": messages})

@login_required
def send_message(request, user_id):

    receiver = User.objects.get(id=user_id)

    if request.method == "POST":
        content = request.POST.get("content")

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )

        return redirect("inbox")

    return render(request, "messaging/send_message.html", {"receiver": receiver})