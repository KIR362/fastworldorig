from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            form.add_error('email', "There's user with this E-MAIL in our database!")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            ins = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            users = authenticate(username=username, password=password, email=email)
            users.profile.avatar = '/static/users/img/standart.jpg'
            ins.email = email
            ins.first_name = first_name
            ins.last_name = last_name
            ins.save()
            form.save_m2m()
            messages.success(request, 'You have registered successfully!')
            login(request, users)
            return redirect('/')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)







