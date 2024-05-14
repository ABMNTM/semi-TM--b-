from django.urls import path , include
from . import views


urlpatterns = [
	# main urls
	path('' , views.BoardCLView.as_view()),
	path('<int:pk>/', views.BoardURDView.as_view()),
	path('project/', views.ProjectCLView.as_view()),
	path('project/<int:pk>/', views.ProjectURDView.as_view()),

	# task urls

	path('task/', include('task.urls')),
]
