from django.urls import path
from . import views
from django.contrib.auth import views as standart_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', standart_views.LoginView.as_view(), name='login'),
    path('logout/', standart_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)