from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='main'),
  path('about', views.reg, name='about'),
  path('set_profile', views.account_setting, name='set'),
  path('user/<int:user_id>', views.user, name='user'),
  path('user/<int:user_id>/follow', views.add_follower, name='follow'),
  path('user/<int:user_id>/unfollow', views.del_follower, name='unfollow'),
  path('report', views.report, name='reporting'),
]