from django.urls import path
from . import views

urlpatterns = [
    path('update-password/' , views.UserPasswordUpdateView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('', views.UserURDView.as_view()),
]