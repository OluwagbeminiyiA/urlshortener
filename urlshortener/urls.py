from django.urls import path
from . import views
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('', views.UrlShortenView.as_view({'post': 'create'}), name='shorten_url'),
    path('<str:key>/', views.UrlRedirectView.as_view({'get': 'retrieve'}), name='original_url'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
