from rest_framework_simplejwt import views
from django.contrib import admin
from django.urls import path , include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
	path('admin/', admin.site.urls),
    path('token/refresh/', views.token_refresh),
    path('token/obtain/', views.token_obtain_pair),
    path('account/', include('account.urls')),
	path('board/' , include('board.urls')),
    path('list/', include('task.urls')),
    # Schemas 
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
