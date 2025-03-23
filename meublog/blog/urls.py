# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', views.detalhe_post, name='detalhe_post'),
    path('criar/', views.criar_post, name='criar_post'),
]
