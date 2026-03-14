from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required


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

@login_required
def conversation(request, user_id):

    other_user = User.objects.get(id=user_id)

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("date")

    return render(request, "messaging/conversation.html", {
        "messages": messages,
        "other_user": other_user
    })
    
@login_required
def conversation(request, user_id):

    other_user = User.objects.get(id=user_id)

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("date")

    return render(request, "messaging/conversation.html", {
        "messages": messages,
        "other_user": other_user
    })
    
@login_required
def inbox(request):
    # tu lógica actual
    return render(request, "messaging/inbox.html")