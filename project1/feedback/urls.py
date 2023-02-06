from django.urls import path
from .views import *

urlpatterns = [
    path('create/', FeedbackCreateApi.as_view()),
    path('show/', FeedbackShowApi.as_view()),
    path('modify/<int:pk>/', FeedbackUpdateApi.as_view()),

]