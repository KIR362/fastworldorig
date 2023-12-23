from django.urls import path
from . import views

urlpatterns = [
  path('', views.news_123, name='news'),
  path('create', views.create, name='create'),
  path('<int:article_id>', views.pub_url, name='pub_detail'),
  path('<int:article_id>/update', views.edit_post, name='pub_update'),
  path('<int:article_id>/delete', views.delete_post, name='pub_delete'),
  path('comment/<int:comment_id>/delete', views.delete_com, name='com_delete'),
]