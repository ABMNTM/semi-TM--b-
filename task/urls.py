from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateList.as_view()),
    path('<int:pk>', views.ListUD.as_view()),
    path('task/', views.TaskCreate.as_view()),
    path('task/<int:pk>', views.TaskURD.as_view())
]
