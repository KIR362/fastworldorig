from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def main_mess(request):
    if not request.user.is_authenticated:
        return redirect('login')
    messages = (Message.objects.filter(sender=request.user) | Message.objects.filter(reciever=request.user)).order_by("-date_stamp")
    users = []
    user = User.objects.get(id=request.user.id)
    last_messages = []
    for message in messages:
        if message.sender != request.user:
            if not message.sender in users:
                users.append(message.sender)
                last_message = (Message.objects.filter(sender=message.sender, reciever=request.user) | Message.objects.filter(reciever=message.sender, sender=request.user)).order_by("-date_stamp")[:1]
                last_messages.append(last_message)
        if message.reciever != request.user:
            if not message.reciever in users:
                users.append(message.reciever)
                last_message = (Message.objects.filter(sender=message.reciever,reciever=request.user) | Message.objects.filter(reciever=message.reciever, sender=request.user)).order_by("-date_stamp")[:1]
                last_messages.append(last_message)
    last_messages_list = []
    for message_query in last_messages:
        for message in message_query:
            if not message.is_readed and message.reciever == request.user:
                last_messages_list.insert(0, message)
            else:
                last_messages_list.append(message)
    return render(request, 'messenger/main_mess.html', {'last_messages_list': last_messages_list, 'user': user})

@login_required(login_url='/')
def chat(request, username):
    if not request.user.is_authenticated:
        return redirect('login')
    companion = User.objects.get(username=username)
    messages1 = Message.objects.filter(sender = request.user, reciever = companion).order_by('date_stamp') | Message.objects.filter(sender = companion, reciever = request.user).order_by('date_stamp')
    not_readed_messages = Message.objects.filter(reciever=request.user, sender=companion, is_readed=False)
    for message in not_readed_messages:
        message.is_readed = True
        message.save()
    form = MessageForm(request.POST)
    if form.is_valid():
        new_mess = form.save(commit=False)
        new_mess.sender = request.user
        new_mess.reciever = companion
        new_mess.save()
        return redirect('dialog', username)
    else:
        error = 'Incorrect message'
    user = User.objects.get(username=request.user)
    form = MessageForm()

    context = {'messages1': messages1, 'form': form, 'username': username, 'user': user}
    return render(request, 'messenger/dialog.html', context)

@login_required(login_url='/')
def delete_mess(request, message_id):
    if not request.user.is_authenticated:
        return redirect('login')
    message = Message.objects.get(id=message_id)
    try:
        if request.user == message.sender or request.user == message.reciever:
            message.delete()
    except:
        if request.user.profile.lang == 'R':
            raise Http404("Сообщение не найдено!")
        else:
            raise Http404("Message hasn't been found!")

    if message.sender == request.user:
        return HttpResponseRedirect(reverse('dialog', args=(message.reciever.username, )))
    else:
        return HttpResponseRedirect(reverse('dialog', args=(message.sender.username, )))
