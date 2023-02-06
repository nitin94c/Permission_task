from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from feedback.views import FeedbackViewSet
from rest_framework_simplejwt.views import token_refresh, token_obtain_pair

# router = DefaultRouter()
# router.register('feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('feedback.urls')),
    path('auth/', include('auth_app.urls')),
    path('access_token/', token_obtain_pair),
    path('refresh_token/', token_refresh),

]
