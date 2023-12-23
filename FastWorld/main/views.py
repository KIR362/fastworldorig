from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ReportForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.apps import apps
from .models import Follower, Profile
from django.db.models import F

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    username = request.user
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'main/main.html', context)

def reg(request):
    if not request.user.is_authenticated:
        return redirect('login')
    username = request.user
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'main/about.html', context)

@login_required(login_url = '/')
def account_setting(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_set = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_set.profile)
        if form.is_valid():
            user_setting = request.user
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            #avatar = form.cleaned_data['avatar']
            gender = form.cleaned_data['gender']
            city = form.cleaned_data['city']
            lang = form.cleaned_data['lang']
            birth_date = form.cleaned_data['birth_date']
            '''if avatar:
                user_setting.profile.avatar = avatar
            else:
                user_setting.profile.avatar = 'images/avatar/standart.jpg'''
            user_setting.profile.gender = gender
            user_setting.profile.city = city
            user_setting.profile.birth_date = birth_date
            user_setting.profile.lang = lang
            if first_name:
                user_setting.first_name = first_name
            if last_name:
                user_setting.last_name = last_name
            user_setting.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = ProfileForm(instance=user_set.profile)
    context = {'form': form, 'user': user_set}
    return render(request, 'main/set_tings.html', context)



def user(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    users = User.objects.get(id=user_id)
    pubs = apps.get_model('news', 'Articles')
    pubs = pubs.objects.filter(owner = users)
    f_count = Profile.objects.get(user = user_id)
    f_count = f_count.followers
    us = User.objects.get(username=request.user)
    if Follower.objects.filter(user=request.user, follower_for=users):
        is_follower = False
    else:
        is_follower = True

    context = {'user': users, 'pubs': pubs, 'f_count': f_count, 'is_fol': is_follower, 'us': us}


    return render(request, 'main/profile.html', context)

def add_follower(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        user = User.objects.get(id=user_id)
    except:
        if request.user.profile.lang == 'R':
            raise Http404("Пользователь не найден!")
        else:
            raise Http404("User hasn't been found!")
    is_follower = Follower.objects.filter(user=request.user, follower_for=user)
    if not is_follower:
        add_follower = Follower(user=request.user, follower_for=user)
        add_follower.save()
        Profile.objects.filter(user=user_id).update(followers=F('followers') + 1)

    return HttpResponseRedirect(reverse('user', args=(user_id, )))

def del_follower(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        user = User.objects.get(id=user_id)
    except:
        if request.user.profile.lang == 'R':
            raise Http404("Пользователь не найден!")
        else:
            raise Http404("User hasn't been found!")

    is_follower = Follower.objects.filter(user=request.user, follower_for=user)
    if is_follower:
        delete_follower = Follower.objects.filter(user=request.user, follower_for=user_id)
        delete_follower.delete()
        Profile.objects.filter(user=user_id).update(followers=F('followers') - 1)

    return HttpResponseRedirect(reverse('user', args=(user_id, )))

def report(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            return redirect('news')
    user = User.objects.get(username=request.user)
    form = ReportForm()
    context = {'form': form, 'user': user}
    return render(request, 'main/report.html', context)
