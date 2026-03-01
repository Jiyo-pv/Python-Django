from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='list'),
    path('add/', views.add_post, name='add'),
    path('post/<int:id>/', views.post_detail, name='detail'),
]