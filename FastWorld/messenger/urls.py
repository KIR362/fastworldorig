from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_mess, name='mess'),
  path('dialog/<str:username>', views.chat, name='dialog'),
  path('dialog/delete_mess/<int:message_id>', views.delete_mess, name='del_mess'),
]