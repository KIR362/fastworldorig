from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import Http404
from django.contrib.auth.models import User

@login_required()
def topics(request):
    if not request.user.is_authenticated:
        return redirect('login')
    topicis = Topic.objects.filter(owner=request.user).order_by('date_added')
    user = User.objects.get(username=request.user)
    context = {'topicis': topicis, 'user': user}
    return render(request, 'topics/topics.html', context)

@login_required()
def topic(request, topic_id):
    if not request.user.is_authenticated:
        return redirect('login')
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    user = User.objects.get(username = request.user)
    context = {'topic': topic, 'entries': entries, 'user': user}
    return render(request, 'topics/topic.html', context)

@login_required()
def new_topic(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')
    user = User.objects.get(username=request.user)
    context = {'form': form, 'user': user}
    return render(request, 'topics/new_topic.html', context)

@login_required()
def new_entry(request, topic_id):
    if not request.user.is_authenticated:
        return redirect('login')

    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id = topic_id)
    user = User.objects.get(username = request.user)
    context = {'topic': topic,'form': form, 'user': user}
    return render(request, 'topics/new_entry.html', context)

