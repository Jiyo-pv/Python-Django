from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_feedback, name='submit'),
    path('all/', views.view_feedback, name='view_feedback'),
]