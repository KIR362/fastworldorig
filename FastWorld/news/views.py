from django.shortcuts import render, redirect
from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm
from django.db.models import F
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

def news_123(request):
    if not request.user.is_authenticated:
        return redirect('login')
    news_123 = Articles.objects.order_by('-title')
    search_query = request.GET.get('search', '')
    if search_query:
        news_123 = Articles.objects.filter(title__icontains = search_query)
    user = User.objects.get(username=request.user)
    context = {'news': news_123, 'user': user}
    return render(request, 'news/news.html', context)

@login_required(login_url='/')
def pub_url(request, article_id):
    if not request.user.is_authenticated:
        return redirect('login')
    article = Articles.objects.get(id=article_id)
    Articles.objects.filter(id=article_id).update(views=F('views') + 1)
    comments = article.comment.order_by()
    form = CommentsForm(request.POST)

    if form.is_valid():
        new_сomment = form.save(commit=False)
        new_сomment.owner = request.user
        new_сomment.article = article
        new_сomment.save()
        return redirect('pub_detail', article_id)
    else:
        error = 'Incorrect publication'
    form = CommentsForm()

    user = User.objects.get(username=request.user)

    if article.owner == request.user:
        context = {'article': article, 'comments': comments, 'form': form, 'owner': True, 'user': user}
    else:
        context = {'article': article, 'comments': comments, 'form': form, 'user': user}
    return render(request, 'news/pub_url.html', context)

@login_required(login_url = '/')
def edit_post(request, article_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        pub = Articles.objects.get(id = article_id)
    except:
        raise Http404("Post hasn't been found!")

    if pub.owner == request.user:
        if request.method == 'POST':
            form = ArticlesForm(request.POST, request.FILES, instance=pub)
            if form.is_valid():
                pub.post_title = form.cleaned_data['title']
                pub.post_text = form.cleaned_data['full_text']
                pub.intro = form.cleaned_data['intro']
                pub.save()
                return HttpResponseRedirect(reverse('news'))
        else:
            form = ArticlesForm(instance=pub)
        user = User.objects.get(username=request.user)
        context = {'form': form, "pub": pub, 'user': user}
        return render(request, 'news/edit_pub.html', context)
    else:
        return HttpResponseRedirect(reverse('news'))

@login_required(login_url = '/')
def delete_post(request, article_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        pub = Articles.objects.get(id = article_id)
    except:
        raise Http404("Post hasn't been found!")
    if pub.owner == request.user:
        pub.delete()
    return HttpResponseRedirect(reverse('news'))

@login_required(login_url = '/')
def delete_com(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        com = Comments.objects.get(id = comment_id)
    except:
        raise Http404("Comment hasn't been found!")
    if com.owner == request.user:
        com.delete()
    return HttpResponseRedirect(reverse('news'))

def create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            new_pub = form.save(commit=False)
            new_pub.owner = request.user
            new_pub.save()
            return redirect('news')
        else:
            error = 'Incorrect publication'
    user = User.objects.get(username = request.user)
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
        'user': user,
    }

    return render(request, 'news/create.html', data)
